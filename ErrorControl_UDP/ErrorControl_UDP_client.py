import random
from socket import * 

port =2500
BUFFER = 1024
server = 'localhost'
c_sock = socket(AF_INET, SOCK_DGRAM)
c_sock.connect((server, port))

for i in range(10):# 10번 시도
    delay = 0.1
    data = 'Hello message'
    
    while True:
        c_sock.send(data.encode())
        print(f'waiting up to {delay} seconds for a reply')
        c_sock.settimeout(delay) # 타임 아웃 설정
        try :
            data = c_sock.recv(BUFFER)
        except timeout:
            delay *= 2
            if delay > 2.0: # 시간초
                print('The server seems to be down')
                break
        else:
            print("Response: ", data.decode())
            break #