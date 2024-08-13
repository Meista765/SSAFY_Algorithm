import sys
sys.stdin = open('input.txt')

from collections import deque



for test_case in range(1,11):
    tc = int(input())
    q = deque(map(int,input().split()))
    flag = True
    while flag:
        for i in range(1,6):
            num = q.popleft()
            num -= i
            if num <= 0:
                num = 0
                q.append(num)
                flag = False
                break
            else:
                q.append(num)
    print(f'#{test_case}', end= ' ')
    print(*q)

