T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))
    max_cnt = 0  # 낙차
    for i in range(N):
        cnt = 0  # arr[i]보다 작은 수 카운트

        for j in range(i + 1, N):
            if arr[i] > arr[j]:
                cnt += 1

        if max_cnt < cnt:
            max_cnt = cnt

    print(f'#{test_case} {max_cnt}')

