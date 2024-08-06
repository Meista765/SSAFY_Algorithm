'''
()()((()))
((()((((()()((()())((())))))
())
(()
'''
# =================================
# stack 직접 구현해서 사용
arr = input()
S = [0] * 100 # 충분히 크게
top = -1    # 초기값, 인덱스 저장
ans = True
for ch in arr:
    if ch == '(':
        top += 1; S[top] = ch
    else:
        if top == -1 or S[top] != '(':
            ans = False
            break
        top -= 1
if top != -1:
    ans = False
print(ans)

# =================================
# List의 append()/pop() 사용
arr = input()
S = []
ans = True
for ch in arr:
    if ch == '(':
        S.append(ch)
    else:
        if not S or S[-1] != '(':
            ans = False
            break
        S.pop()
if S:
    ans = False
print(ans)
# =====================================

