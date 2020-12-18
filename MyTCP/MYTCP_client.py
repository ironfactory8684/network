# MYTCP_client.py
# 명령 인수를 받아 실행되는 클라이언트 프로그램

import socket
import sys
import argparse

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 명령 인수 -s, -p 정의
parser = argparse.ArgumentParser()
parser.add_argument('-s', default='127.0.0.1') #서버 지정 인수
parser.add_argument('-p', default='2500') #서버 지정 인수
args = parser.parse_args() # 인수를 저장하는 객체

sock.connect((args.s, int(args.p)))
print("connected to ",args.s)

# 메시지를 송신하고 수신 메시지를 출력한다.
while True:
    sendData = input("sending message: " )
    if not sendData:
        continue
    if sendData == 'q':
        break
        print("연결을 종료합니다.")
    sock.send(sendData.encode())
    print("Received message: {}".format(sock.recv(1024).decode()))

sock.close()