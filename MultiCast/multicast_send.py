# 멀티캐스트 전송 프로그램
from socket import *
import struct 

group_addr = ("224.0.0.255", 5005) # 그룹주소
s_sock =socket(AF_INET, SOCK_DGRAM) # UDP 소켓 사용
s_sock.settimeout(0.5)

TTL= struct.pack("@i", 2)
s_sock.setsockopt(IPPROTO_IP, IP_MULTICAST_TTL, TTL)

while True:
    rmsg = input('your message:')
    s_sock.sendto(rmsg.encode(), group_addr)
    while True:
        try:
            #모든 수신자로부터 응답
            response, addr = s_sock.recvfrom(1024)
        except timeout: 
            break
        else:
            #응답 출력
            print("{} from {}".format(response.decode(), addr))