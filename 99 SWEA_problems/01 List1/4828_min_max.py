import sys; sys.stdin = open('4828.txt')


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))

    min_val = 1e10      # N최대 1000, 입력 최대 1000000
    max_val = 0         # 입력값 최소 1

    for val in arr:
        if min_val > val:
            min_val = val
        if max_val < val:
            max_val = val
            
    print(f'#{tc} {max_val - min_val}')