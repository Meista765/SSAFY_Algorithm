import sys; sys.stdin = open('1206.txt', 'r')

for tc in range(1, 11):
    # 하나의 테스트 케이스
    N = int(input())   # 자료수
    arr = list(map(int, input().split()))
    ans = 0
    for i in range(2, N - 3 + 1):
        max_val = arr[i - 2]
        for val in [arr[i - 1], arr[i + 1], arr[i + 2]]:
            if max_val < val:
                max_val = val

        # --------------------------------------------------------------
        if arr[i] > max_val:
            ans += arr[i] - max_val
    print(f'#{tc} {ans}')