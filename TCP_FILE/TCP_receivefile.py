# TCP_receivefile.py
# 파일 수신 프로그램

import socket

s_sock = socket.socket()
host = 'localhost'
port = 2500

s_sock.connect((host, port))
s_sock.send("i am ready".encode())
fn = s_sock.recv(1024).decode()

with open('./data/'+fn, 'wb') as f:
    print('file opened')
    print('receiveing file....')
    while True:
        data = s_sock.recv(8192) # 파일 내용수신
        if not data:
            break
        f.write(data)

print('Download complete')
s_sock.close()
print("Connection closed")
