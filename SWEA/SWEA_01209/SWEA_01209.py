import sys
sys.stdin = open("C:/Users/SSAFY/Desktop/스터디/SSAFY_Algorithm/SWEA/SWEA_01209/input.txt", "r")
# input = sys.stdin.readline

n = 100
for _ in range(10):
    tc = int(input())
    matrix = [list(map(int, input().split())) for _ in range(n)]

    max_sum = float('-inf')
    # 행 합
    for i in range(n):
        row_i = matrix[i]
        row_sum = 0
        for j in range(n):
            row_sum += row_i[j]
        if max_sum < row_sum:
            max_sum = row_sum

    # 열 합
    for j in range(n):
        col_sum = 0
        for i in range(n):
            row_i = matrix[i]
            col_sum += row_i[j]
        if max_sum < col_sum:
            max_sum = col_sum

    # 대각 합
    ## 오른쪽
    diagonal_sum_1 = 0
    for i in range(n):
        for j in range(n):
            if i == j:
                diagonal_sum_1 += matrix[i][j]
    if max_sum < diagonal_sum_1:
        max_sum = diagonal_sum_1
     
    ## 왼쪽
    diagonal_sum_2 = 0
    for i in range(n):
        for j in range(n):
            if (n - 1 - i) == j:
                diagonal_sum_2 += matrix[i][j]
    if max_sum < diagonal_sum_2:
        max_sum = diagonal_sum_2

    print(f'#{tc} {max_sum}')