from web3 import Web3
from web3.auto import w3
import os

public_rpc_url = "https://eth-mainnet.alchemyapi.io/v2/QYHyUFgB_x9GST0m4N-bTkTmeM_fxDbO"
web3 = Web3(Web3.HTTPProvider(public_rpc_url))


while True:
    # Kiểm tra kết nối thành công
    if web3.is_connected():
        print("Connected to Ethereum network")
    else:
        print("Failed to connect to Ethereum network")
        exit(1)

    # Tạo private key ngẫu nhiên
    account = w3.eth.account.create()
    private_key = account.key

    # Địa chỉ ví Ethereum được tạo từ private key
    address = account.address

    # Lấy số dư và chuyển đổi sang Wei
    balance = web3.eth.get_balance(address)
    print("Private key: ", private_key.hex())
    print(f"Số dư của địa chỉ {address} là: {balance} Wei")

    # Lưu vào file nếu số dư lớn hơn 0
    if balance >= 0:
        with open("data.txt", "a") as file:
            file.write(
                f"Address: {address}, Balance: {balance} Wei, Private Key: {private_key.hex()}\n"
            )
