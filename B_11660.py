import sys
input = sys.stdin.readline

N,M = map(int,input().split())

# 인덱스 계산하기 편하게 0을 추가해서 행렬을 만듬

m = [[0]*(N+2)]+[[0] +list(map(int,input().split()))+ [0] for _ in range(N)] + [[0]*(N+2)]

matrix_sum = [[0] * (N+2) for _ in range(N+2)]
num = 0

# 구간 합 matrix 만들기

for i in range(1,N+1):
    for j in range(1,N+1):
        matrix_sum[i][j] = matrix_sum[i-1][j] + matrix_sum[i][j-1] - matrix_sum[i-1][j-1] + m[i][j]
        
# 구간 합을 이용한 결과 구하기

for _ in range(M):
    x1, y1, x2, y2 = map(int,input().split())
    
    answer = matrix_sum[x2][y2] - matrix_sum[x1-1][y2] - matrix_sum[x2][y1-1] + matrix_sum[x1-1][y1-1]
    print(answer)
        


        
        
        
