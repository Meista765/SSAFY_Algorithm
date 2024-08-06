icp = {'(': 3, ')': 3, '*': 2, '/': 2, '+': 1, '-': 1} # stack에 push하기 전
isp = {'(': 0, ')': 3, '*': 2, '/': 2, '+': 1, '-': 1} # 스택에 내부
# infix = '(6+5*(2-8)/2)+6'
infix = '6*5+(2-8)/2+6'
S = []          # 스택
postfix = ''    # 후위표기법 저장
for token in infix:
    if token in icp:   # 연산자
        if token == ')':
            while S and S[-1] != '(':
                postfix += S.pop()
            S.pop()
        else:   # (*/+-
            # token 과 스택의 꼭대기 있는 연산자의 우선순위 비교
            while S and icp[token] <= isp[S[-1]]:
                postfix += S.pop()
            S.append(token)
    else:              # 피연산자
        postfix += token

while S:
    postfix += S.pop()

print('후위표기', postfix)



'''
[2단계] 후위표기법 수식을 계산 
1) 피연산자를 만나면 스택에 push 한다. 
2) 연산자를 만나면 필요한 만큼의 피연산자를 스택에서 pop하여 연산하고, 연산결과를 다시 스택에 push 한다. 
3) 수식이 끝나면, 마지막으로 스택을 pop하여 출력한다.
'''

for token in postfix:
    if token in icp:
        b, a = S.pop(), S.pop()
        if token == '+': S.append(a + b)
        elif token == '*': S.append(a * b)
        elif token == '-': S.append(a - b)
        else: S.append(a / b)
    else:
        S.append(int(token))

print(S.pop())