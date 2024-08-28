def dfs(v):
    global cnt
    if v > N:
        return
 
    dfs(v*2)
    tree[v] = cnt
    cnt += 1
    dfs(v*2 + 1)
 
T = int(input())
for test_case in range(1,T+1):
    N = int(input())
    tree = [0] * (N+1)
    cnt = 1
    dfs(1)
 
    print(f'#{test_case} {tree[1]} {tree[N//2]}')