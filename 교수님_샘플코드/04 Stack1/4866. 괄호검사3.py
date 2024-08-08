import sys; sys.stdin = open('4866.txt', 'r')

L = {'{': '}', '(': ')'}
R = {'}': '{', ')': '('}
def check_paren(arr):
    S = []
    for ch in arr:
        if ch in L:
            S.append(ch)
        elif ch in R:
            if not S or S[-1] != R[ch]:
                return 0
            S.pop()
    if S:
        return 0
    return 1

T = int(input())
for tc in range(1, T + 1):
    arr = input()
    ans = check_paren(arr)
    print(f'#{tc} {ans}')