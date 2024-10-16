import sys
sys.stdin = open('sample_input.txt', 'r')

def permutation(k, N):
    global min_sum
    sum_value = 0
    if k == N:
        for i in range(N):
            sum_value +=  matrix[i][arr[i]]
            if sum_value > min_sum:
                return
        if sum_value < min_sum:
            min_sum = sum_value
            return
    else:
        for i in range(k, N):
            arr[k], arr[i] = arr[i], arr[k]
            permutation(k + 1, N)
            arr[k], arr[i] = arr[i], arr[k] 

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    arr = list(range(N))
    min_sum = 10 * N
    
    permutation(0, N)
    
    print(f'#{tc} {min_sum}')



