def dfs(v):
    global cnt
 
    if L[v] != 0 and R[v] != 0:    # 양쪽에 자식이 있으면
        cnt += 2
        dfs(L[v])
        dfs(R[v])
 
    elif L[v] != 0:  # 왼쪽에 자식이 있으면
        cnt += 1
        dfs(L[v])
    elif R[v] != 0:  # 오른쪽에 자식이 있으면
        cnt += 1
        dfs(R[v])
    else:           # 둘다 없으면 종료
        return
 
 
 
 
 
T = int(input())
for test_case in range(1,T+1):
    E, N = map(int,input().split())     # E: 간선의 수, N: 루트 노드 번호
    edges = list(map(int,input().split()))  # 간선의 정보
 
    L = [0] * (E+1+1)   # 왼쪽 자식
    R = [0] * (E+1+1)   # 오른쪽 자식
    P = [0] * (E+1+1)   # 부모 정보
 
 
    for i in range(0,E*2, 2):
        p, c = edges[i], edges[i + 1]
 
        if L[p] == 0:  # 왼쪽자식이 없으면
            L[p] = c
        else:
            R[p] = c
        P[c] = p
 
 
    cnt = 1
    dfs(N)
    print(f'#{test_case} {cnt}')