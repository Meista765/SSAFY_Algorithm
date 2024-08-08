
def change(lst):
    stack = []
    result = ''

    for token in lst:
        if not stack:               # 스택이 비어있다면
            if token == '+':        # token이 + 이면
                stack.append(token) # stack에 append
            else:
                result += token

        else:                       # 스택이 비어있지 않다면
            if token == '+':
                result += stack.pop()
                stack.append(token)
            else:
                result += token
    return result + stack.pop()

def my_calculate(t):

    stack = []

    for token in t:
        if token == '+':
            v1,v2 = stack.pop(), stack.pop()
            stack.append(v2 + v1)
        else:
            stack.append(int(token))
    return stack.pop()


for test_case in range(1,11):
    N = int(input())
    lst = list(input())
    print(f'#{test_case} {my_calculate(change(lst))}')
