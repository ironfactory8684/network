# TCP_client_demo.py
# 간단한 TCP 클라이언트

import socket

#TCP 소켓을 생성하여 서버와 연결
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 서버주소 입력
svrIP = input(("Server IP(default:127.0.0.1): "))
if svrIP == '':
    svrIP = '127.0.0.1'

# 포트번호 입력
port = input(("port (default:2500): "))
if port == '':
    port = 2500
else:
    port = int(port)
    
s.connect((svrIP, port))
print('Connected to '+ svrIP)

#전송 메시지를 입력받아 보내고 수신메시지를 출력한다.
while True:
    msg = input("message to send: ")

    # 송신 데이터 값으면 다시 진행
    if not msg:
        continue
    
    try:
        s.send(msg.encode()) # 메시지 전송
    except:
        print("연결이 종료 되었습니다.")
        break
    
    try:
        msg = s.recv(1024)
        if not msg:
            print("연결이 종료되었습니다.")
            break
        print("Received message: {}".format(msg.decode()))

    except:
        print("연결이 종료되었습니다.")
        break
s.close()