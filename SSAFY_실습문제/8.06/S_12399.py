import sys
sys.stdin = open('input.txt')

T = int(input())

for test_case in range(1,T+1):
    text = input()
    stack =[]


    for ch in text:
        if not stack: # 스택이 비어있다면
            stack.append(ch)
        else:         # 스택이 비어있지 않다면
            if stack[-1] == ch:  # 스택의 top과 ch를 비교
                stack.pop()
            else:
                stack.append(ch)

    print(f'#{test_case} {len(stack)}')
