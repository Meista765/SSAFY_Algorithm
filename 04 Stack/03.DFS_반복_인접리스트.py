import sys; sys.stdin = open('graph_input.txt', 'r', encoding='utf-8')
V, E = map(int, input().split()) # 정점수, 간선수
G = [[] for _ in range(V+1)]   # 인접 리스트
arr = list(map(int, input().split())) # 크기 = 2*E

for i in range(0, 2*E, 2):
    u, v = arr[i], arr[i + 1]
    G[u].append(v)
    G[v].append(u)

S = []   # 스택
visited = [0] * (V + 1) # 정점번호는 1 ~ V까지

# 1) 시작 정점 v를 결정하여 방문한다.
v = 1
visited[v] = 1; print(v, end=' ') # 방문

while True:
    for w in G[v]:
        if not visited[w]:
            S.append(v)
            visited[w] = 1; print(w, end=' ')
            v = w
            break
    else:
        if not S:
            break
        v = S.pop()