import sys; sys.stdin = open("4837.txt", "r")

for tc in range(1, int(input()) + 1):
    N, K = map(int, input().split())    # N: 부분집합의 원소 수, K: 원소의 합

    # 모든 부분집합 생성
    ans = 0
    for bit in range(1 << 12):
        S = cnt = 0
        for i in range(12):
            if bit & (1 << i):
                S += i + 1
                cnt += 1

        if cnt == N and S == K:
            ans += 1

    print(f'#{tc} {ans}')
