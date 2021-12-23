# Import libraries
import socket
import os
import shutil
from pathlib import Path


dirname = os.path.join(os.getcwd(), 'files')

def process(req):
    req = req.split()
    if req[0] == 'pwd':
        return dirname
    elif req[0] == 'ls':
        return '; '.join(os.listdir(dirname))
    elif req[0] == 'mkdir':
        try:
            if not os.path.exists(os.path.join(dirname, req[1])):
                os.makedirs(os.path.join(dirname, req[1]))
                return os.path.join(dirname, req[1])
            else:
                return "Aleady exists"
        except:
            return "Missing arguments!"
    elif req[0] == 'cat':
        filename = os.path.join(os.getcwd(), 'docs')+file_name
        try:
            f = open(filename, "r")
            msg = f.read()
            return str(msg)
        except:
            return 'Bad file request!'
    elif req[0] == 'mv':
        try:
            src_path = os.path.join(dirname, req[1])
            new_path = os.path.join(dirname, req[2])
            shutil.move(new_path, dst_path)
        except:
            return 'Bad path request!'
    elif req[0] == 'rm':
        try:
            path = os.path.join(dirname, req[1])
            os.remove(path)
        except:
            return 'Bad request!'
    elif req[0] == 'touch':
        try:
            path = os.path.join(dirname, req[1])
            my_file = open(path)
            writing = os.path.join(dirname, req[2])
            my_file.write(writing)
            my_file.close()
        except:
            return 'Bad file request!'
    elif req[0] == 'break':
        return 'break'
    else:
        return 'bad request'


PORT = 1703

sock = socket.socket()
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sock.bind(('', PORT))
sock.listen()
print("Запущен сервер. Прослушивается порт: ", PORT)

flag = True
while flag:
    conn, addr = sock.accept()
    
    request = conn.recv(1024).decode()
    print(request)
    
    response = process(request)
    conn.send(response.encode())
    if response[0] == 'break':
        flag = False
conn.close()
