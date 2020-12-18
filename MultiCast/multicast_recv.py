# 멀티캐스트 수신 프로그램
from socket import *
import struct # 가입할 그룹 주소를 바이너리로 표현

BUFFER = 1024
group_addr = "224.0.0.255" #그룹 주소
r_sock =socket(AF_INET, SOCK_DGRAM)
r_sock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
r_sock.bind(("", 5005))

merq = struct.pack('4sl', inet_aton(group_addr), INADDR_ANY)
# inet_aton함수는 점 표기법 주소를 32비트 압축형 바이너리 주소로 변환해주는 역할
# INADDR_ANY는 빈 문자열을 의미
r_sock.setsockopt(IPPROTO_IP, IP_ADD_MEMBERSHIP, merq) # 그룹 가입
print('ready to receive')

while True:
    rmsg, addr = r_sock.recvfrom(BUFFER) # 멀티캐스트 메시지 수신
    print("Received '{}' from ({}, {})".format(rmsg.decode(), *addr))
    r_sock.sendto("ACK".encode(), addr)