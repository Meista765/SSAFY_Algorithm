T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    arr = [[0] * N for _ in range(N)]

    dr = [0, 1, 0, -1]  # 우 -> 하 -> 좌 -> 상
    dc = [1, 0, -1, 0]

    r, c = 0, 0
    d = 0  # 변화
    for i in range(1, N * N + 1):
        arr[r][c] = i
        r += dr[d]
        c += dc[d]
        if r < 0 or c < 0 or r >= N or c >= N or arr[r][c] != 0:  # 인덱스를 벗어나거나 이미 지나온 곳이면
            # 실행 취소
            r -= dr[d]
            c -= dc[d]

            d = (d + 1) % 4

            r += dr[d]
            c += dc[d]

    print(f'#{test_case}')
    for j in arr:
        print(*j)
