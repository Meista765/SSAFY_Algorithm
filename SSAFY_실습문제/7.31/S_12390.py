import sys
sys.stdin = open('input.txt','r')

T = int(input())

for test_case in range(1,T+1):
    N, K = map(int,input().split())

    arr = list(range(1,13))

    # 12-N
    cnt = 0

    for i in range(0,12-N+1):
        s = 0 # 부분 집합의 합
        for j in range(0,3):
            s += arr[i+j]
        if s == K:
            cnt += 1
    print(f'#{test_case} {cnt}')