T = int(input())

for test_case in range(1,T+1):
    N, M = map(int,input().split())
    matrix = [[0] * (N + M*2) for _ in range(M)] + [[0] * M + list(map(int, input().split())) + [0] * M for _ in range(N)] + [[0] * (N + M*2) for _ in range(M)]

    #matrix = [list(map(int, input().split())) for _ in range(N)]

    sum_matrix = [[0]*(N+M*2) for _ in range(N+M*2)]
    
    
    # 구간 합 구하기
    for i in range(M,len(matrix)-M+1):
        for j in range(M,len(matrix)-M+1):
            sum_matrix[i][j] = sum_matrix[i-1][j] + sum_matrix[i][j-1] - sum_matrix[i-1][j-1] + matrix[i][j]
 

    # 
    max_fly = 0
    for i in range(M,len(matrix)-M+1):
        for j in range(M,len(matrix)-M+1):
            now_fly = sum_matrix[i][j]-sum_matrix[i-M][j]-sum_matrix[i][j-M]+sum_matrix[i-M][j-M]
            if max_fly < now_fly:
                max_fly = now_fly
    print(f'#{test_case} {max_fly}')