import sys
sys.stdin = open('input.txt')

T = int(input())
for test_case in range(1,T+1):
    t = input()
    N = len(t)
    stack = []
    cnt = 0

    idx = 0                                             # 인덱스

    while idx < N:

        if t[idx] == '(' and t[idx+1] == ')':           # ()는 레이저 
            cnt += len(stack)                           # ()를 만나면 스택안에 '('의 갯수만큼 cnt에 더하기
            idx += 2                                    # 이후 인덱스를 2칸 이동
            continue

        if t[idx] == '(':                               # '(' 만 만난다면 stack에 추가
            stack.append(t[idx])
        elif t[idx] == ')':                             # ')'를 만나면 stack의 top위치에 있는 것을 pop한 후 cnt에 +1
            stack.pop()
            cnt += 1
        idx += 1
    

    print(f'#{test_case} {cnt}')
