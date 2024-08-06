# ==============================
# 저장소 - 전역변수, 함수 구현
N = 5
S = [0] * N
top = -1
def isEmpty():
    return top == -1

def push(item):
    global top
    if top == N - 1:
        return  # overflow - 가득 차 있다
    top += 1
    S[top] = item

def my_pop():
    global top
    if top == -1:
        print('underflow')
        return 0 # empty
    ret = S[top]
    top -= 1
    return ret
#==================================
for i in range(3):
    push(i + 1)

while top != -1:
    print(my_pop())
# while not isEmpty():
#     print(pop())
# =====================================
# 직접 index를 조작해서 push, pop 을 구현
N = 5
S = [0] * N
top = -1

for i in range(3):
    top += 1
    S[top] = i + 1

while top != -1:
    print(S[top])
    top -= 1
# =====================================
# List의 append(), pop() 활용
S = []
for i in range(3):
    S.append(i + 1)

while S:
    print(S.pop())