from socket import *
from select import * 

socks = []
sock = socket()
sock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
socks.append(sock)
sock.connect(('localhost', 2500))

while True:
    r_sock, w_sock, e_sock = select(socks, [],[] , 0)
    if r_sock:
        for s in r_sock:
            if s==sock:
                msg = sock.recv(1024).decode()
                print("수신 메시지 : ", msg)
    smsg = input('전송 메시지: ')
    sock.send(smsg.encode())