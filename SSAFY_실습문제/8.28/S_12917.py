def dfs(v):
    if v > N:
        return 0
 
    left = dfs(v*2)
    right = dfs(v*2+1)
    tree[v] += left + right
    return tree[v]
 
 
 
 
T = int(input())
 
for test_case in range(1,T+1):
    N, M, L = map(int,input().split())
    tree = [0] * (N+1)
 
    for _ in range(M):
        i, val = map(int,input().split())
        tree[i] = val
    dfs(1)
    print(f'#{test_case} {tree[L]}')