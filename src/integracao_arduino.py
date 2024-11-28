import pyfirmata2
import os
from dotenv import load_dotenv

load_dotenv()


porta_serial, pino_fechadura = os.getenv("PORTA_SERIAL"), os.getenv("PINO_FECHADURA")



try:
    # PORTA SERIAL (USB) ONDE O ARDUINO ESTÁ CONECTADO
    board = pyfirmata2.Arduino("COM3")

    # PINO ONDE SERÁ FEITO O CONTROLE DA FECHADURA
    fechadura = board.get_pin('d:3:o') 
except:
    print("Não foi possível conectar ao Arduino")



def abrir_fechadura():
    print("Fechadura aberta")
    fechadura.write(1)

def fechar_fechadura():
    print("Fechadura fechada")
    fechadura.write(0)