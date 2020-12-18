#TCP 에코서버
# 1명의 클라이언트만 서비스한다.

from socket import *
port = 2500
BUFSIZE = 1024 

sock= socket(AF_INET, SOCK_STREAM)
sock.bind(('', port)) # 자신의 주소 사용
sock.listen(1) # 최대 대기 클라이언트 수
print("Waiting for client ...")

# 클라이언트의 연결 요청을 받는다.
c_sock, (r_host, r_port) = sock.accept()
print("connected by", r_host, r_port)

while True:
    try:
        # 상대방 메시지 수신
        data = c_sock.recv(BUFSIZE)
        if not data: # 연결이 종료되었으면
            print("1연결이 종료되었습니다.")
            c_sock.close()
            break
    except:
        print("2연결이 종료되었습니다.")
        c_sock.close() # 소켓을 닫는다.
        break # 무한루프 종료
    else:
        print("Recevied message:",data.decode())
    
    try:
        c_sock.send(data)
    except : # 연결 종료로 인한 예외 발생
        print("3연결이 종료되었습니다.")
        c_sock.close() # 소켓을 닫는다.
        break # 무한 루프 종료
