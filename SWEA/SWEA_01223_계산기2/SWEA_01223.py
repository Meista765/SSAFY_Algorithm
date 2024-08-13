import sys
sys.stdin = open('C:/Users/SSAFY/Desktop/깃/SSAFY_Algorithm/SWEA/SWEA_01223_계산기2/input.txt', 'r')

icp = {'*': 2, '+': 1} # stack에 push하기 전
isp = {'*': 2, '+': 1} # 스택에 내부

for tc in range(1, 11):
    N = int(input())
    infix = input()
    
    # 후위식 만들기
    postfix = ''
    stack = []

    for token in infix:
        if token in icp:
            # icp가 isp보다 커질 때 까지 pop, stack에 뭐가 있어야 비교 함
            while  stack and icp[token] <= isp[stack[-1]]:
                postfix += stack.pop()
            # 그 외 push
            stack.append(token)
        # 피연산자
        else:
            postfix += token

    # 계산하기
    cal_stack = []

    for token in postfix:
        # 연산자 계산
        if token in icp:
            b, a = stack.pop(); stack.pop()
            if token == '+':
                cal_stack.append(a + b)
            elif token == '*':
                cal_stack.append(a * b)
        # 피연산자
        else:
            cal_stack.append(int(token))

    print(f'#{tc} {cal_stack.pop()}')
