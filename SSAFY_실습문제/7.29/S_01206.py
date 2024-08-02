T = 10

for test_case in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))

    result = 0  # 조망권이 확보된 세대 수

    for i in range(2, N - 2):
        if arr[i] - arr[i - 2] > 0 and arr[i] - arr[i - 1] > 0 and arr[i] - arr[i + 1] > 0 and arr[i] - arr[i + 2] > 0:
            min_num = arr[i] - arr[i - 2]  # 초기값 설정
            for j in [-1, 1, 2]:
                if min_num > arr[i] - arr[i + j]:
                    min_num = arr[i] - arr[i + j]
            result += min_num
    print(f'#{test_case} {result}')