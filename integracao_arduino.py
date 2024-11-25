import pyfirmata2

board = pyfirmata2.Arduino("COM3") # PORTA SERIAL 5 É ONDE O ARDUINO ESTÁ CONECTADO
fechadura = board.get_pin('d:3:o') # PINO 3 É UTILIZADO PARA CONTROLE DA FECHADURA


def abrir_fechadura():
    print("Fechadura aberta")
    fechadura.write(1)

def fechar_fechadura():
    print("Fechadura fechada")
    fechadura.write(0)