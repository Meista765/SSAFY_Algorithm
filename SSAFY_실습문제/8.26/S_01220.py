# 1: N극 2: S극
import sys
sys.stdin = open('input.txt')
for test_case in range(1,11):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]
    cnt = 0         # 교착 상태

    for j in range(N):
        np = 0          # N극 표시
        for i in range(N):
            if arr[i][j] == 1:
                np = 1
            elif arr[i][j] == 2 and np: # 교착상태
                cnt += 1
                np = 0
    print(f'#{test_case} {cnt}')

