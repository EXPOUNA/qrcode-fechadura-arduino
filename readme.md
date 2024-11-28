# ABERTURA DE FECHADURA COM QR-CODE

Este projeto foi desenvolvido com o objetivo de criar um sistema de segurança para controle de acesso, utilizando uma fechadura solenoide, QR Codes para autenticação, e Arduino com Python para integração e controle. O sistema realiza a leitura de códigos QR por meio de uma câmera, verifica a validade dos códigos consultando um banco de dados no Supabase, e, se o código for válido, aciona a fechadura solenoide para liberar o acesso.

A comunicação entre o Arduino e o Python é feita usando a biblioteca PyFirmata no lado do Python e a biblioteca Firmata no Arduino, garantindo uma integração simples e eficiente. A leitura dos QR Codes é realizada com a biblioteca OpenCV, combinada com a pyzbar, para uma detecção rápida e precisa dos códigos.

Como Funciona:
Leitura do QR Code: O código QR é lido pela câmera conectada ao computador, usando a biblioteca OpenCV e pyzbar.
Validação no Supabase: Após a leitura, o código QR é comparado com os registros armazenados em um banco de dados no Supabase, garantindo que o código seja válido.
Acionamento da Fechadura: Se o código for autenticado com sucesso, o sistema envia um sinal para o Arduino, que por sua vez envia um sinal 5V ao transistor permitindo a passagem de corrente até a fechadura solenoide, fazendo a abertura da mesma.

![ESQUEMA ELETRÔNICO FECHADURA SOLENOIDE + ARDUINO](https://github.com/user-attachments/assets/d416cb2b-0a92-4b0e-b1ec-6ac5c3220cd5)

## Requisitos

- Python 3.10
- PyFirmata2
- OpenCV2
- PySerial
- Supabase

## Instalação

Siga os passos abaixo para configurar o ambiente de desenvolvimento.

### 1. Clonar o repositório

Clone o repositório para o seu computador:

```bash
git clone https://github.com/EXPOUNA/qrcode-fechadura-arduino.git
```

Configure o ambiente virtual

```bash
python -m venv .venv
```

Inicie o ambiente virtual

Windows

```bash
.\.venv\Scripts\activate
```

Linux

```bash
source .venv/bin/activate
```

## Configuração do projeto

- Criar um arquivo .env seguindo o modelo .env.example
- Preencher as credenciais do banco, chave secreta do qr code, porta serial e pino do arduino

## Inicializar o projeto

```bash
py .
```
OU
```bash
py __main__.py
```

## Sair do projeto

-Pressione ESC dentro da janela da câmera
-Pressione CTRL + V no terminal onde o programa está sendo executado
