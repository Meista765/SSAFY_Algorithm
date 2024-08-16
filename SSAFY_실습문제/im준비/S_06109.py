def up(arr,N):

    for j in range(N):
        for i in range(1,N):
            # 위에가 같은 숫자면
            if arr[i][j] == arr[i-1][j]:
                arr[i-1][j] += arr[i][j]
                arr[i][j] = 0

            # 위에가 0 이면
            elif arr[i-1][j] == 0:
                arr[i-1][j] += arr[i][j]
                arr[i][j] = 0

    # 마지막에 0자리 채우기
    for j in range(N):
        for i in range(1,N):




T = int(input())
for test_case in range(1,T+1):
    N, direction = input().split()
    N = int(N)

    arr = [list(map(int,input().split())) for _ in range(N)]
