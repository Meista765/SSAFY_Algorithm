import sys
input = sys.stdin.readline

N = int(input())
lst = [0] * N    # 수열 리스트
result = []     # print할 결과
stack = []      # stack
flag = True     # NO를 print한지를 알아보는 flag 변수
num = 1     # stack에 넣을 자연수

for i in range(N):
    lst[i] = int(input())   # 수열 리스트에 값 넣기

for i in range(N):      # 수열 리스트에 있는 개수만큼 반복
    if lst[i] >= num:       
        while lst[i] >= num:
            stack.append(num)
            num += 1
            result += '+'
        stack.pop()
        result += '-'
    else:
        temp = stack.pop()
        if temp > lst[i]:
            print('NO')
            flag = False
            break
        else:
            result += '-'

if flag:    # NO를 print한적 없으면 result 출력
    for i in result:
        print(i)