import sys; sys.stdin = open('4873.txt', 'r')

for tc in range(1, int(input()) + 1):
    arr = input()
    S = []
    for ch in arr:
        if not S:
            S.append(ch)
        elif S[-1] != ch:
            S.append(ch)
        else:
            S.pop()
    print('#{} {}'.format(tc, len(S)))
