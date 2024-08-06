# 스택 - Last in First out
# 자료구조: 저장소 + 연산(push, pop)



# 저장소
print('첫 번째 방법')
N = 5
S = [0] * N     # 0부터 N - 1까지
top = -1        # top은 꼭대기 값의 인덱스를 저장, 초기값은 -1(빈스택을 의미함)

def push(item):
    global top
    # if top == N - 1:
    #     print('overflow')
    #     return
    top += 1
    S[top] = item

def my_pop():   # top 값을 가져오기 때문에 인자가 필요 없다
    global top
    # empty 상황 체크
    # if top == -1:
    #     print('underflow')
    #     return 
    ret = S[top]
    top -= 1
    return ret

def isEmpty():
    return top == -1

push(1);push(2);push(3)

while not isEmpty():
    print(my_pop())


# ===================================
print('두 번째 방법')
N = 5
S = [0] * 5
top = -1

# push
top += 1; S[top] = 1
top += 1; S[top] = 2
top += 1; S[top] = 3

# pop
while top != -1:
    print(S[top]); top -= 1

# ===================================
print('세 번째 방법')

S = []
S.append(1)
S.append(2)
S.append(3)

while S:
    print(S.pop())