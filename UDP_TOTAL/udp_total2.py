import argparse, random, socket, sys

BUFFSIZE = 2048

def Server(ipaddr, port): # 서버함수
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind((ipaddr, port))
    print(sock.getsockname(), "에서 대기 중...")

    while True:
        data, address = sock.recvfrom(BUFFSIZE)
        if random.random() <0.5: # 랜덤 넘버가 < 0.5이면 다시 수신
            print("{}에서 패킷 수신".format(address))
            continue
        text = data.decode("utf-8")
        print("{}에서 클라이언트가 보낸 메시지:{!r}".format(address, text))
        message = '데이터의 길이는 {} 바이트 임'.format(len(data))
        sock.sendto(message.encode('utf-8'), address)


def Client(hostname, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.connect((hostname, port)) 
    print('클라이언트 소켓 이름은 {}입니다.'.format(sock.getsockname()))

    delay = 0.1
    text = '저는 클라이언트 입니다.'
    data = text.encode('utf-8')
    while True:
        sock.send(data)
        print('{}초 동안 응답 대기'.format(delay))
        sock.settimeout(delay)
        try:
            data = sock.recv(BUFFSIZE)
        except socket.timeout as exc:
            delay *=2
            if delay >2.0:
                raise RuntimeError("서버가 다운되었습니다.") from exc
        else:
            break
    print("서버 응답: {!r}".format(data.decode("utf-8")))

if __name__ == '__main__':
    mode = {'c': Client, 's':Server}
    parser = argparse.ArgumentParser(description='Send and receive UDP,' 'pretending packets are often dropped') # 명령인수 해석 객체
    parser.add_argument('role', choices =mode, help='client or server')
    parser.add_argument('host', help="server interface" "host the client sends to")
    parser.add_argument('-p', metavar='PORT', type=int,
            default =2500, help='UDP port (default 2500)') # 옵션인수
    args = parser.parse_args()
    operation = mode[args.role]
    operation(args.host, args.p)