import sys; sys.stdin = open("4839.txt", "r")

# 재귀
def binary_search(lo, hi, key):

    if lo > hi: return -1
    mid = (lo + hi) >> 1
    if key == mid:
        return 1
    if key < mid:
        return binary_search(lo, mid, key) + 1
    else:
        return binary_search(mid, hi, key) + 1


T = int(input())
for tc in range(1, T + 1):
    P, A, B = map(int, input().split())

    cntA = binary_search(1, P, A)
    cntB = binary_search(1, P, B)

    ans = 0
    if cntA < cntB: ans = 'A'
    elif cntA > cntB: ans = 'B'

    print(f'#{tc} {ans}')

