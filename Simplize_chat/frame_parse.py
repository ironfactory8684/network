import socket
import capsule

Size = 5
sock = socket.socket()
sock.connect(('localhost', 2500))

HEAD = 0x05
addr =1 
seqNo = 1
frame_seq = ""
msg ='hello world'
print("전송 메시지:", msg)
for i in range(0, len(msg), Size):
    start = i
    frame_seq += capsule.frame(HEAD, addr, seqNo, msg[start:start+Size])
    start += Size
    seqNo += 1

sock.send(frame_seq.encode()) 
msg = sock.recv(2048).decode()
print("수신 프레임:", msg)

r_frame = msg.split(chr(0x05))
del r_frame[0]

p_msg = ""


for fr in r_frame:
    p_msg += fr[10:(11+int(fr[6:10]))]
print("복원 메시지:", p_msg)
sock.close()