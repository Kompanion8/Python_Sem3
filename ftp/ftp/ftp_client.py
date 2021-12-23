# Import libraries
import socket
import os

HOST = 'localhost'
PORT = 1703
print("Запущен клиент. Прослушивается порт: ", PORT)

while True:
    try:
        request = input('>')
    except:
        break
    sock = socket.socket()
    try:
        sock.connect((HOST, PORT))
    except:
        break   
    sock.send(request.encode())
    try:
        response = sock.recv(1024).decode()
    except:
        break
    if response == 'exit' or response == 'break':
        break
    print(response)
    
    sock.close()