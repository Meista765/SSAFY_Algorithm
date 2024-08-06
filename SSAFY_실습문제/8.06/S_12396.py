
T = int(input())

for test_case in range(1,T+1):
    string = input()
    stack = []

    for s in string:
        if not stack:    # 스택이 빈 리스트 라면
            if s in ['{','}','(',')']: # s가 괄호문자인지 확인
                stack.append(s)
        elif s in ['{','}','(',')']: # 스택이 빈 리스트가 아니면서 s가 괄호문자인지 확인
            if (stack[-1] == '{' and s == '}') or (stack[-1] == '(' and s == ')'): # 괄호의 짝이 맞으면  pop
                stack.pop()
            else:
                stack.append(s)

    if stack:
        print(f'#{test_case} 0')
    else:
        print(f'#{test_case} 1')






