import os
from dotenv import load_dotenv

load_dotenv()
QR_SECRET = os.getenv("QR_SECRET")

from src.leitor import camera

camera()