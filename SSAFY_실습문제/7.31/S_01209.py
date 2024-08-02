import sys
sys.stdin = open('input.txt', 'r')

for test_case in range(1,11):
    N = int(input()) # testcase번호

    arr = [list(map(int,input().split())) for _ in range(100)]

    max_val = 0

    # 행 방향 합
    for r in range(100):
        s = 0
        for c in range(100):
            s += arr[r][c]
        if max_val < s:
            max_val = s

    # 열 방향 합
    for r in range(100):
        s = 0
        for c in range(100):
            s += arr[c][r]
        if max_val < s:
            max_val =s

    # 좌상 -> 우하 대각선 합
    s = 0
    for r in range(100):

        for c in range(100):

            if r == c:
                s += arr[r][c]

        if max_val < s:
            max_val = s


    # 우상 -> 좌하 대각선 합
    s = 0
    for r in range(100):

        for c in range(100-1,-1,-1):

            if r == c:
                s += arr[r][c]

        if max_val < s:
            max_val = s

    print(f'#{test_case} {max_val}')
