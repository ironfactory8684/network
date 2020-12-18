import random
from socket import * 
port =2500
BUFFER =1024

s_sock = socket(AF_INET, SOCK_DGRAM)
s_sock.bind(("", port))
print("Waiting...")

while True:
    data, address = s_sock.recvfrom(BUFFER)
    if random.randint(1,10):
        print('Packet from {} lost!!!'.format(address))
        continue
    print(f"Message is {data.decode()!r} from {address}")
    
    s_sock.sendto("ACK".encode(), address) # ACK 응답 전송