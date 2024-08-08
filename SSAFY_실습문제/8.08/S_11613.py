def my_calculate(lst):

    stack = []
    cal_lst = ['+', '-', '*', '/']

    for token in lst:
        if token in cal_lst:
            if len(stack) >= 2:
                if token == '+':
                    v1, v2 = stack.pop(), stack.pop()
                    stack.append(v2 + v1)
                elif token == '-':
                    v1, v2 = stack.pop(), stack.pop()
                    stack.append(v2 - v1)
                elif token == '*':
                    v1, v2 = stack.pop(), stack.pop()
                    stack.append(v2 * v1)
                elif token == '/':
                    v1, v2 = stack.pop(), stack.pop()
                    stack.append(v2 // v1)
            else:
                return 'error'
        else:
            if token == '.':
                if len(stack) == 1:
                    return stack.pop()
                else:
                    return 'error'
            else:
                stack.append(int(token))


T = int(input())

for test_case in range(1,T+1):

    lst = list(input().split())
    result = my_calculate(lst)
    print(f'#{test_case} {result}')


