import sys
#input = sys.stdin.readline
sys.stdin = open("C:/Users/USER/Desktop/input.txt", "r")

T = int(input())

for idx in range(1,T+1):
    N, M = map(int, input().split())

    A = [[0]*(N+1)]
    D = [[0]*(N+1) for _ in range(N+1)]

    for _ in range(N):
        A_row = [0] + [int(x) for x in input().split()]
        A.append(A_row)
    #print(A)

    for i in range(1, N+1):
        for j in range(1, N+1):
            D[i][j] = D[i-1][j] + D[i][j-1] - D[i-1][j-1] + A[i][j]
    #print(D)


    max_value = 0
    for i in range(M, N+1):
        for j in range(M, N+1):
            '''if j == M:
                temp = D[i][j] - D[i-M][j]
            else:
                temp = D[i][j] - D[i][j-M] - D[i-M][j] + D[i-M][j-M]'''
            temp = D[i][j] - D[i][j-M] - D[i-M][j] + D[i-M][j-M]
            if max_value < temp:
                max_value = temp
    print(f'#{idx} {max_value}')


        


