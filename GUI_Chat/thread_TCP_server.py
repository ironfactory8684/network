# _thread 
# threading

from socket import *
import _thread

BUFFSIZE = 1024
host_addr = '127.0.0.1'
port = 2500

def response(key):
    return "서버 응답 메시지"

def handler(clientsock, addr):
    while True:
        data = clientsock.recv(BUFFSIZE) # 데이터 수신
        print('data: ' + repr(response('')))
        if not data: break
        clientsock.send(response('').encode()) # 응답 전송
        print('sent : '+ repr(response('')))

if __name__ == '__main__':
    ADDR = (host_addr, port)
    serversock = socket(AF_INET, SOCK_STREAM)
    serversock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    serversock.bind(ADDR)
    serversock.listen(5)

    while True:
        print('waiting for connection..')
        clientsock, addr = serversock.accept()
        print('...connected from: ', addr)
        _thread.start_new_thread(handler, (clientsock, addr)) # 스레드 생성 실행