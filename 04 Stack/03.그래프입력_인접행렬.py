import sys; sys.stdin = open('graph_input.txt', 'r', encoding='utf-8')

V, E = map(int, input().split())    # 정점수, 간선수
G = [[0] * (V + 1) for _ in range(V + 1)]   # 인접 행렬

arr = list(map(int, input().split()))
# 간선수만큼 입력 처리
for i in range(0, E*2, 2):
    u, v = arr[i], arr[i + 1]
    G[u][v] = 1
    G[v][u] = 1

for lst in G[1:]:
    print(*lst[1:])




