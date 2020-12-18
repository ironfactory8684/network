import select, socket, sys, queue

s_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s_sock.setblocking(0) # 블록킹 모드
s_sock.bind(('localhost', 2500))
s_sock.listen(5)

r_socks = [s_sock] #수신 소켓 목록, 서버 소켓 추가
w_socks = [] # 송신 소켓 목록
msgQueues = {} # 메시지 큐의 목록 {소켓 : 메시지큐}

while r_socks:
    readEvent, writeEvent, errorEvent = select.select(
        r_socks, w_socks, r_socks
    )
    for s in readEvent:
        if s is s_sock: #서버 소켓인가?
            c_sock, c_address = s.accept()
            c_sock.setblocking(0) # 블록킹 모드
            r_socks.append(c_sock)
            msgQueues[c_sock] = queue.Queue()

        else:
            data = s.recv(1024)
            if data:
                msgQueues[s].put(data)
                if s not in w_socks:
                    w_socks.append(s)
            else:
                if s in w_socks:
                    w_socks.remove(s)
                r_socks.remove(s)
                s.close()
                del msgQueues[s]
    for s in writeEvent:
        try:
            next_msg = msgQueues[s].get_nowait()
        except queue.Empty:
            w_socks.remove(s)
        else:
            s.send(next_msg)
    for s in errorEvent:
        r_socks.remove(s)
        if s in w_socks:
            w_socks.remove(s)
        s.close()
        del msgQueues[s]
