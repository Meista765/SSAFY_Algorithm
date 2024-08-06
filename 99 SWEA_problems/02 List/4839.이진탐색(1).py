import sys; sys.stdin = open("4839.txt", "r")

T = int(input())
for tc in range(1, T + 1):
    P, A, B = map(int, input().split())

    def binary_search(P, key):
        lo, hi = 1, P
        cnt = 0
        while lo <= hi:
            mid = (lo + hi) >> 1
            cnt += 1
            if key == mid:
                return cnt
            elif key < mid:
                hi = mid
            else:
                lo = mid

        return -1

    cntA = binary_search(P, A)
    cntB = binary_search(P, B)

    ans = 0
    if cntA < cntB: ans = 'A'
    elif cntA > cntB: ans = 'B'

    print(f'#{tc} {ans}')

