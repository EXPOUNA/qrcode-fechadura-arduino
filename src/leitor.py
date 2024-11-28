import time
import cv2


from pyzbar import pyzbar


from integracao_arduino import *
from verificacao_qr import confirmar_usuario_qr
from tratar_qr import decodificar_json




def cam_decode(frame):
    # Processa o frame para detectar e decodificar códigos QR.

    barcodes = pyzbar.decode(frame)
    for barcode in barcodes:
        x, y, w, h = barcode.rect
        barcode_info = barcode.data.decode('utf-8')
        # Desenha o retângulo em torno do código
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)
        return frame, barcode_info
    
    return frame, None 

def camera(qr_secret):
    try:
        fechadura_aberta = False
        t_fechadura = 0
        camera = cv2.VideoCapture(0)
        last_qr = None

        while True:
            ret, frame = camera.read()
            if not ret:
                print("Erro: Falha ao capturar o frame da câmera.")
                break

            frame, info = cam_decode(frame)

            if info and last_qr != info:
                last_qr = info
                print(f"QR Code detectado: {info}")
                
                qr_data = decodificar_json(info)

                if not qr_data:
                    print("Erro: QR Code inválido.")
                    continue

                if qr_data.get("verify") != qr_secret:
                    print("QR Code com verificação inválida.")
                    continue
                
                if not fechadura_aberta:
                    usuario = confirmar_usuario_qr(qr_data.get("ra"))
                    if usuario:
                        fechadura_aberta = True
                        t_fechadura = time.time()

            # Verifica se o tempo para fechar a fechadura já passou
            if fechadura_aberta and time.time() - t_fechadura >= 10:
                last_qr = None
                fechar_fechadura()
                fechadura_aberta = False

            # Exibe o frame na janela
            cv2.imshow('Leitor de QR Code', frame)
            if cv2.waitKey(1) & 0xFF == 27:  # Pressione 'ESC' para sair
                break
    except Exception as e:
        print(f"leitor - Ocorreu um erro: {e}")
    finally:
        # Libera a câmera e fecha a janela
        camera.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    camera()
