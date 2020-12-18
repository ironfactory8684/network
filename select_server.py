import socket, select
if __name__ == "__main__":
    scoks = [] # 읽기 가능 소켓 목록
    BUFFER = 1024
    port =2500
    s_sock = socket.socket() 
    s_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s_sock.bind(('localhost', port))
    s_sock.listen(5)

    scoks.append(s_sock) # 서버 소켓을 목록에 추가
    print(str(port)+" 에서 접속 대기 중")

    while True:
        #연결 요청 및 수신 대기(읽기 기능 이벤트만 조사)
        r_sock, w_sock, e_sock = select.select(scoks, [], [])

        for s in r_sock: #수신 소켓 리스트의 소켓 조사
            if s== s_sock:#연결요청인가?
                c_sock, addr = s_sock.accept() # 새로운 클라이언트 연결
                scoks.append(c_sock)
                print(" client (%s, %s) connected"%(addr))
            else:
                try:
                    data = s.recv(BUFFER) #데이터 수신
                    print("Received: ", data.decode())
                    if data:
                        s.send(data) # 수신 데이터를 다시 전송
                except:
                    print("Client (%s, %s) is offline"%addr)
                    s.close()
                    scoks.remove(s)
                    continue
    s_sock.close()