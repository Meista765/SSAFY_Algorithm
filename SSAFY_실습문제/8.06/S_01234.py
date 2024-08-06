import sys
sys.stdin = open('input.txt')

for test_case in range(1,11):
    N, number = input().split()
    N = int(N)

    stack = []

    for i in range(N):
        if not stack: # 스택이 비어있다면
            stack.append(number[i])
        else:         # 스택이 비어있지 않다면
            if stack[-1] == number[i]: # 스택이 비어있지 않고 스택의 TOP이 들어올 수와 같다면 pop
                stack.pop()
            else:
                stack.append(number[i])

    print(f'#{test_case} {"".join(stack)}' )

