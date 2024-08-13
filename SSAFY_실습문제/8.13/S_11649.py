# 큐 구현
def enqueue(item):
    global rear
    if is_full():
        return
    rear += 1
    q[rear] = item


def dequeue():
    global front
    if is_empty():
        return
    front += 1
    return q[front]

def is_full():
    if rear == q_size-1:
        return True
    else:
        return False

def is_empty():
    if front == rear:
        return True
    else:
        return False

import sys
sys.stdin = open('input.txt')


T = int(input())

for test_case in range(1,T+1):
    N, M = map(int,input().split())
    arr = list(map(int,input().split()))
    q_size = 1001
    q = [0] * q_size
    front = rear = -1

    for i in range(N):
        enqueue(arr[i])

    for _ in range(M):
        enqueue(dequeue())

    print(f'#{test_case} {dequeue()}')
