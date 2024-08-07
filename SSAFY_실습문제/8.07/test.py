'''
7 8
1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7
'''
def DFS(v):               # s = 시작정점, v= 정점개수
    visited[v] = 1 # 시작지점 방문표시
    print(v, end=' ')
    for w in adj_list[v]:
        if not visited[w]:
            DFS(w)





T = int(input())
for test_case in range(1,T+1):
    v, e = map(int,input().split())     # 정점,간선
    arr = list(map(int, input().split()))
    adj_list = [[] for _ in range(v+1)] # 인접리스트
    visited = [0] * (v + 1)             # 방문리스트
    for i in range(e):
        u, v = arr[i*2], arr[i*2+1]
        adj_list[u].append(v)
        adj_list[v].append(u)
    DFS(1)
