N = int(input())
arr = list(map(int,input().split())) 
ans = [0] * N # 정답 리스트
stack = []    #    

for i in range(N):
    while stack and arr[stack[-1]] < arr[i]: # 스택의 top 값이 새로 들어올 값보다 작다면 오큰수
        ans[stack.pop()] = arr[i]            # 스택의 top 값을 pop하고 ans에 입력
    stack.append(i)    # 아니라면 append

    
while stack: # 반복문이 다 종료됐는데 stack에 값이 남아있다면 스택에 남아있는 index는 -1
    ans[stack.pop()] = -1

print(*ans)