import sys; sys.stdin = open('4831.txt')

T = int(input())
for tc in range(1, T + 1):
    K, N, M = map(int, input().split())
    arr = list(map(int, input().split()))

    cur = 0  # 현재 정류장번호
    ans = 0  # 충전횟수
    while cur + K < N:
        for next in range(cur + K, cur, -1):
            if next in arr:
                ans += 1
                cur = next
                break
        else:
            ans = 0
            break

    print(f'#{tc} {ans}')







