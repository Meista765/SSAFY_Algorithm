import sys
sys.stdin = open('input.txt')

# 원형 큐
def enqueue(item):
    global rear
    if is_full():
        return
    rear = (rear+1) % (N+1)
    q[rear] = item

def dequeue():
    global front
    if is_empty():
        return
    front = (front+1) % (N+1)
    return q[front]

def is_full():
    if front == (rear+1) % (N+1):
        return True
    else:
        False

def is_empty():
    if front == rear:
        return True
    else:
        False


T = int(input())

for test_case in range(1,T+1):
    N = int(input())
    q = [0] * (N+1)
    front = rear = 0

    for i in range(1,N+1):
        enqueue(i)

    while True:   # 큐에 값이 하나 남았을 때까지
        dequeue()
        if rear - front == 1:
            break
        else:
            enqueue((dequeue()))

    print(f'#{test_case} {q[rear]}')

