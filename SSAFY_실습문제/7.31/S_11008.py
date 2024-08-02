import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for test_case in range(1,T+1):

    N = int(input()) # 2차원 배열의 길이

    matrix = [list(map(int,input().split())) for _ in range(N)] # 입력받은 데이터

    # 본인상하좌우
    dr = [-1,1,0,0]
    dc = [0,0,-1,1]
    max_val = 0 # 자기 자신과 이웃 원소의 합 중 최대값
    for i in range(N):
        for j in range(N):
            s = matrix[i][j] # 자기 자신과 이웃 원소의 합
            for k in range(4):# 인덱스를 수정해 가면서 이웃 원소의 합 구하기
                nr = i + dr[k] 
                nc = j + dc[k]

                if 0 <= nr <N and 0<= nc < N: # 넘어가는 인덱스를 잡기 위해 
                    s += matrix[nr][nc]

            if max_val < s:
                max_val = s
    print(f'#{test_case} {max_val}')

