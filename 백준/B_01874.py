
# 이 방식으로 다시 풀어보자
'''N = int(input())

arr = [0] * N
#  4, 3, 6, 8, 7, 5, 2, 1
for i in range(N):
    arr[i] = int(input())

stack = []
answer = ''
num = 1
idx = 0

for target in arr:
    
    while target not in stack: # stack에 target이 없다면 target이 들어갈 때까지 append
        stack.append(num)
        num += 1
        answer += '+\n'

    
    while target in stack: # stack에 target이 있다면 target이 나올 때까지 pop
        t = stack.pop() 
        answer += '-\n'
        if target == t:
            break
    if target '''  
    
import sys
input = sys.stdin.readline   
N = int(input())
A = [0] * N

for i in range(N):
    A[i] = int(input())

stack = []
num =1
answer = ''
flag = True

for i in range(N):
    target = A[i]
    if target >=num:
        while target >= num:
            stack.append(num)
            num += 1
            answer += '+\n'

        stack.pop()
        answer += '-\n'

    else:
        n = stack.pop()

        if n > target:
            print('NO')
            flag = False
            break
        else:
            answer += '-\n'
if flag:
    print(answer)

    


    


