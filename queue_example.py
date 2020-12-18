import queue
fifo_q = queue.Queue() #FIFO 큐 생성
data = ["Hello", "World", 'Python', "Koread]
for value in data: # 큐에 저장
    fifo_q.put(value)

while not fifo_q.empty() # 큐에 저장된 값이 있는지 확인
    print(fifo_q.get())