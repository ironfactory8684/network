# TCP_client_demo.py
# 간단한 TCP 클라이언트

import socket
port = 2500
address = ("localhost", port)
BUFSIZE = 1024

#TCP 소켓을 생성하여 서버와 연결
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(address)

#전송 메시지를 입력받아 보내고 수신메시지를 출력한다.
while True:
    msg = input("message to send: ")
    s.send(msg.encode()) # 서버로 메시지 송신
    r_msg = s.recv(BUFSIZE) # 서버로부터 메시지 수신
    if not r_msg:break # 연결이 해제되었으므로 종료
    print("Received message: %s"%r_msg.decode())
