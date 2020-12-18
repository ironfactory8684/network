# TCP_sendfile.py
# 파일 전송 프로그램

import socket
import sys

port =2500
s_sock = socket.socket()
host = ''
s_sock.bind((host, port))
s_sock.listen(1)

c_sock, addr = s_sock.accept()
print('Connected from ', addr)
msg = c_sock.recv(1024) 
print(msg.decode())
filename = input('file name to send(./sample.bin): ')
print("sending {}".format(filename))
fn = filename.split('/')

c_sock.sendall(fn[-1].encode())

with open(filename, 'rb') as f:
    c_sock.sendfile(f,0) # 파일 내용 전송

print('sending complete')
c_sock.close()