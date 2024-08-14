#=======================================
# 원형큐
QSIZE = 4
Q = [0] * QSIZE
front = rear = 0
# front가 가리키는 곳은 첫번째 요소의 앞(빈공간)
def enqueue(item):
    global rear
    # full 인지 체크, front == (rear + 1) % QSIZE
    if front == (rear + 1) % QSIZE:
        return
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

# ==================================
enqueue(1); print(Q)
enqueue(2); print(Q)
enqueue(3); print(Q)
enqueue(4); print(Q)    # full

while not isEmpty():
    print(dequeue())