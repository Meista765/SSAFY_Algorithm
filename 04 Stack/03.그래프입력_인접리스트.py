import sys; sys.stdin = open('graph_input.txt', 'r', encoding='utf-8')


# 인접 리스트
#===========================================================

V, E = map(int, input().split())    # 정점수, 간선수
G = [[] for _ in range(V + 1)]   # 인접 행렬

arr = list(map(int, input().split()))
# 간선수만큼 입력 처리
for i in range(0, E*2, 2):
    u, v = arr[i], arr[i + 1]
    G[u].append(v)
    G[v].append(u)

for i in range(1, V + 1):
    print(i, '-->', G[i])



