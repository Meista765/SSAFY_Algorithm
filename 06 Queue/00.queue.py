
# from time import time
# start = time()
# arr = []
# for i in range(100000):
#     arr.append(i)
#
# while arr:
#     arr.pop(0)
# print(time() - start)

#=============================
# 선형큐
from time import time
start = time()
Q = [0] * 1000000
front = rear = -1
# front가 가리키는 곳은 첫번째 요소의 앞(빈공간)
def enqueue(item):
    global rear
    # full 인지 체크, rear == 마지막 인덱스
    rear = rear + 1
    Q[rear] = item
def dequeue():
    global front
    # empty 인지 체크  front == rear
    front = front + 1
    return Q[front]

def isEmpty():
    return front == rear
for i in range(1000000):
    enqueue(i)
while not isEmpty():
    dequeue()
print(time() - start) # 제일 느림
#==========================================
def isFull():
    return rear == len(Q) - 1

def Qpeek():
    if isEmpty(): print('Queue_Empty')
    else: return Q[front + 1]
#==========================================
# 함수를 사용하지 않고
from time import time
start = time()
# 선형큐
Q = [0] * 1000000
front = rear = -1
# front가 가리키는 곳은 첫번째 요소의 앞(빈공간)

for i in range(1000000):
    rear += 1
    Q[rear] = i
while front != rear:
    front += 1
    Q[front]

print(time() - start) # 위에보다 빠름

# ===============================
# 너를 위해 준비했어~~ double ended queue
from collections import deque
from time import time
start = time()

Q = deque()
for i in range(1000000):
    Q.append(i)

while Q:
    Q.popleft()

print(time() - start) # 굉장히 빠름

#=======================================
# 원형큐
QSIZE = 4
Q = [0] * QSIZE
front = rear = 0
# front가 가리키는 곳은 첫번째 요소의 앞(빈공간)
def enqueue(item):
    global rear
    # full 인지 체크, front == (rear + 1) % QSIZE
    rear = (rear + 1) % QSIZE
    Q[rear] = item
def dequeue():
    global front
    # empty 인지 체크  front == rear
    front = (front + 1) % QSIZE
    return Q[front]
def isFull():
    return front == (rear + 1) % QSIZE
def isEmpty():
    return front == rear

enqueue(1)
enqueue(2)
enqueue(3)
print(Q)
print(isFull()) # True

'''
선형 큐, 원형 큐의 isFull, isEmpty 함수는 bool을 결과로 낸다
'''