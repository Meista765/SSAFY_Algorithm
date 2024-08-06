import sys; sys.stdin = open('graph_input.txt', 'r', encoding='utf-8')

#=====================================================
# 그래프 인접리스트로 저장
V, E = map(int, input().split())    # 정점수, 간선수
arr = list(map(int, input().split())) # 크기 = 2*E

G = [[] for _ in range(V + 1)]
visited = [0] * (V + 1)

for i in range(0, 2*E, 2):
    u, v = arr[i], arr[i + 1]
    G[u].append(v)
    G[v].append(u)

def dfs(v): # v = 방문할 정점 번호
    visited[v] = 1 # v를 방문한다.
    print(v, end=' ')
    # v의 인접 정점을 w를 찾는다.
    for w in G[v]:
        if not visited[w]:
            dfs(w)
dfs(1)




