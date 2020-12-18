import argparse, socket
from datetime import datetime

BUFFSIZE = 2048

def Server(port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind(('localhost', port))
    print('{}에서 대기중...'.format(sock.getsockname()))
    while True:
        data, address = sock.recvfrom(BUFFSIZE)
        text = data.decode("utf-8")
        print("{} 클라이언트 메시지 {!r}".format(address, text))
        text = '데이터의 길이는 {} 바이트임'.format(len(data))
        data = text.encode('utf-8')
        sock.sendto(data, address)

def Client(port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    text = '현재 시간은 {}'.format(datetime.now())
    data = text.encode('utf-8')
    sock.sendto(data, ("localhost", port))
    print("운영체제로부터 할당받은 주소는 {}".format(sock.getsockname()))
    data, address = sock.recvfrom(BUFFSIZE)
    text = data.decode('utf-8')
    print("서버 {}의 응답은 {!r}입니다.".format(address, text))

if __name__ == '__main__':
    mode = {'c': Client, 's':Server}
    parser = argparse.ArgumentParser() # 명령인수 해석 객체
    parser.add_argument('role', choices =["c","s"],
            help='client or server')
    parser.add_argument('-p', metavar='PORT', type=int,
            default =2500, help='UDP port (default 2500)') # 옵션인수
    args = parser.parse_args()
    operation = mode[args.role]
    operation(args.p)