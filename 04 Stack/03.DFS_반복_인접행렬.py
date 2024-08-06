import sys; sys.stdin = open('graph_input.txt', 'r', encoding='utf-8')

V, E = map(int, input().split())    # 정점수, 간선수
G = [[0] * (V + 1) for _ in range(V + 1)]   # 인접 행렬
visited = [0] * (V + 1)

arr = list(map(int, input().split()))

for i in range(0, E*2, 2):
    u, v = arr[i], arr[i + 1]
    G[u][v] = G[v][u] = 1

# 1) 시작 정점 v를 결정하여 방문한다.
v = 1
S = [0]      # 스택
visited[v] = 1; print(v, end=' ')
while S:  # 3) 스택이 공백이 될 때까지 2)를 반복한다.
    # 2) 정점 v에 인접한 정점 중에서
    # 방문하지 않은 정점 w가 있으면, 정점 v를 스택에 push하고
    # 정점 w를 방문한다. 그리고 w를 v로 하여 다시 2)를 반복한다.
    # print(S)
    for w in range(1, V + 1):
        if G[v][w] == 1 and visited[w] == 0:
            S.append(v)
            visited[w] = 1; print(w, end=' ')
            v = w
            break
    else:
        # 방문하지 않은 정점이 없으면, 탐색의 방향을 바꾸기 위해서
        # 스택을 pop하여 받은 가장 마지막 방문 정점을 v로 하여 다시 2)를 반복한다.
        v = S.pop()



