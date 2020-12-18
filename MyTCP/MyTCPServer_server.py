#MyTCPServer_server.py
# 사용자 정의 모듈을 이용한 에코 서버 프로그램
import MyTCPServer as mt 
import sys

port =2500
if len(sys.argv) >1: # 명령 실행시 포트를 지정하면 지정 포트 사용
    port = int(eval (sys.argv[1]))
s_sock = mt.TCPServer(port)
c_sock, addr = s_sock.Accept() # 클라이언트 연결

while True:
    print('Connected by', addr[0], addr[1]) # 클라이언트 주소와 포트
    data = c_sock.recv(1024)
    if not data:
        break
    print('Received message:', data.decode())
    c_sock.send(data) # 데이터 재전송
c_sock.close()