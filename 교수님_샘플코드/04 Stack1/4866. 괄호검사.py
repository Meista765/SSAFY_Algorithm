import sys; sys.stdin = open('4866.txt', 'r')

def check_paren(arr):
    S = [0] * 100
    top = -1
    for ch in arr:
        if ch in '({':
            top += 1; S[top] = ch
        elif ch == ')':
            if top == -1 or S[top] != '(':
                return 0
            top -= 1
        elif ch == '}':
            if top == -1 or S[top] != '{':
                return 0
            top -= 1
    if top != -1:
        return 0
    return 1

T = int(input())
for tc in range(1, T + 1):
    arr = input()
    ans = check_paren(arr)
    print(f'#{tc} {ans}')