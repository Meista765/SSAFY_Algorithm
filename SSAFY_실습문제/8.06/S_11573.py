import sys
sys.stdin = open('input.txt')

# push
def push(item):
    global top

    top += 1
    stack[top] = item

# pop
def pop():
    global top

    ret = stack[top]
    top -= 1
    return ret

# 빈 스택인지 확인
def isEmpty():
    return top == -1




T = int(input())

for test_case in range(1,T+1):

    N = int(input())
    top = -1
    stack = [0] * N
    arr = list(map(int,input().split()))

    for i in range(N):
        if arr[i] == 0:
            pop()

        else:
            push(arr[i])
    answer = 0
    while not isEmpty():
        answer += pop()

    print(f'#{test_case} {answer}')