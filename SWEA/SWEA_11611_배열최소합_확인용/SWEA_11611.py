import sys
sys.stdin = open('C:/Users/SSAFY/Desktop/깃/SSAFY_Algorithm/SWEA/SWEA_11611_배열최소합_확인용/sample_input.txt', 'r')

def permutation(k, N):
    # 외부 변수 호출
    global min_sum
    sum_value = 0
    if k == N:
        for i in range(N):
            sum_value +=  matrix[i][arr[i]]
            # 더하는 중에 min_sum 넘어가면 다음 반복
            ## 교수님 코드 참고
            if sum_value > min_sum:
                break
        if sum_value < min_sum:
            min_sum = sum_value
    else:
        for i in range(k, N):
            arr[k], arr[i] = arr[i], arr[k]
            permutation(k + 1, N)
            arr[k], arr[i] = arr[i], arr[k]
    return min_sum

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    arr = list(range(N))
    min_sum = float('inf')
    
    minimum = permutation(0, N)
    
    print(f'#{tc} {minimum}')