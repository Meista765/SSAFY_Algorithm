import sys
sys.stdin = open('input.txt')
T = int(input())

for test_case in range(1,T+1):
    N = int(input())
    arr = [list(map(int,input())) for _ in range(N)]
    s = N // 2
    e = N // 2
    total = 0

    for i in range(N):
        for j in range(s,e+1):
            total += arr[i][j]

        if i < N//2:
            s -= 1
            e += 1
        else:
            s += 1
            e -= 1
    print(f'#{test_case} {total}')