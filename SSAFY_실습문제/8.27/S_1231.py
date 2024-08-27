# 루트 정점의 번호는 항상 1
 
def dfs(v):
    if v == 0:
        return
    dfs(L[v])
    print(alpha[v],end='')
    dfs(R[v])
 
 
for test_case in range(1,11):
    N = int(input())    # 정점의 수
 
    L = [0] * (N+1)     # 왼쪽 자식
    R = [0] * (N+1)     # 오른쪽 자식
    alpha = [0] * (N+1)     # 알파벳 정보
 
    for _ in range(N):
        lst = input().split()
        if len(lst) == 4:   # 양쪽 자식을 가지는 경우
            L[int(lst[0])] = int(lst[2])
            R[int(lst[0])] = int(lst[3])
            alpha[int(lst[0])] = lst[1]
        elif len(lst) == 3: # 왼쪽만 자식을 가지는 경우
            L[int(lst[0])] = int(lst[2])
            alpha[int(lst[0])] = lst[1]
 
        else:
            alpha[int(lst[0])] = lst[1]
    print(f'#{test_case}', end = ' ')
    dfs(1)
    print()