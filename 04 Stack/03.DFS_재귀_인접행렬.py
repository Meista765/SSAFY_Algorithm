import sys; sys.stdin = open('graph_input.txt', 'r', encoding='utf-8')

#=====================================================
# 그래프 인접행렬로 저장
V, E = map(int, input().split())    # 정점수, 간선수
arr = list(map(int, input().split())) # 크기 = 2*E

G = [[0] * (V + 1) for _ in range(V + 1)]   # 인접 행렬
visited = [0] * (V + 1)

for i in range(0, 2*E, 2):
    u, v = arr[i], arr[i + 1]
    G[u][v] = G[v][u] = 1

def dfs(v):
    visited[v] = 1; print(v, end=' ')
    for w in range(1, V + 1):
        if G[v][w] == 1 and not visited[w]:
            dfs(w)

dfs(1)



