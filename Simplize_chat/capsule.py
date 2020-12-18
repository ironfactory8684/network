def frame(start_ch, addr, seqNo, msg): #프레임 구성 함수
    addr = str(addr).zfill(2)
    seqNo = str(seqNo).zfill(4)
    length = str(len(msg)).zfill(4)
    return chr(start_ch)+addr+seqNo+length+ msg

if __name__ == '__main__':
    start_ch = 0x05
    addr = 2
    seqNo = 1

    msg = input("your message:")
    capsule = frame(start_ch, addr, seqNo, msg)
    print(capsule)