import socket

messages = ["Привет, сервер!", "Как дела?"]

for message in messages:

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    server_address = ('localhost', 12345)
    client_socket.connect(server_address)

    client_socket.send(message.encode())

    response = client_socket.recv(1024).decode()
    print(f"Ответ от сервера: {response}")

    client_socket.close()
