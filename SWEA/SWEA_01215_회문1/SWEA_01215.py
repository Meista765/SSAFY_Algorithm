import sys
sys.stdin = open('C:/Users/SSAFY/Desktop/git/SSAFY_Algorithm/SWEA/SWEA_01215_회문1/input.txt', 'r')

for tc in range(1, 11):
    N = 8
    M = int(input())
    matrix = [list(input()) for _ in range(N)]

    cnt = 0

    # 행 탐색
    for i in range(N):  # i: 0 ~ N-1
        for j in range(N-M+1):  # j: 0 ~ N-M
            for d in range(M//2):
                nj1 = j + d
                nj2 = j + (M-1) - d
                if matrix[i][nj1] != matrix[i][nj2]:
                    break
            else: cnt += 1


    # 열 탐색
    for j in range(N):
        for i in range(N-M+1):
            for d in range(M//2):
                ni1 = i + d
                ni2 = i + (M-1) - d
                if matrix[ni1][j] != matrix[ni2][j]:
                    break
            else: cnt += 1
    
    print(f'#{tc} {cnt}')