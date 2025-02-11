# 브로드 캐스트 송신 프로그램

from socket import * 
# addr = ('192.168.0.255', 10000) # 브로드캐스트 주소
addr = ('<broadcast>', 10000)

# 브로드캐스팅을 위한 소켓 설정
s = socket(AF_INET, SOCK_DGRAM)
s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
s.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)
# SOL_SOCKET 소켓 관련 옵션 
# SO_REUSEADDR 소켓 주소 재사용
# SO_BROADCAST 브로드 캐스트 사용여부 

while True:
    smsg = input('Broadcast Message: ')
    s.sendto(smsg.encode(), (addr)) # 브로드캐스팅 메시지 전송