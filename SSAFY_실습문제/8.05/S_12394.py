import sys
sys.stdin = open('input.txt')
T = int(input())

for test_case in range(1,T+1):
    N, M = map(int,input().split())
    arr = [input() for _ in range(N)]

    answer = ''
    # 행탐색
    for i in range(N):
        for j in range(N-M+1):
            for k in range(M//2):
                if arr[i][j+k] != arr[i][j+M-1-k]:

                    break
            else:
                for d in range(M):
                    answer += arr[i][j+d]


    # 열 탐색
    for j in range(N):
        for i in range(N-M+1):
            for k in range(M//2):
                if arr[i+k][j] != arr[i+M-1-k][j]:
                    break
            else:
                for d in range(M):
                    answer += arr[i+d][j]

    print(f'#{test_case} {answer}')
