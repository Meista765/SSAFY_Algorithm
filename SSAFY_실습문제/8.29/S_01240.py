import sys
sys.stdin = open('input.txt')

T = int(input())
for test_case in range(1,T+1):
    N, M = map(int,input().split())
    arr = [list(input().strip()) for _ in range(N)]

    for i in range(N):
        for j in range(M-1,-1,-1):
            if arr[i][j] == 1:
                for