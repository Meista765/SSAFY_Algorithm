import sys; sys.stdin = open('graph_input.txt', 'r')

V, E = map(int, input().split())
G = [[] for _ in range(V + 1)]
arr = list(map(int, input().split()))
for i in range(0, E*2, 2):
    u, v = arr[i], arr[i + 1]
    G[u].append(v)
    G[v].append(u)

#=======================================
def BFS1(s):
    visit = [0] * (V + 1)
    D = [0] * (V + 1)  # 시작점에서 최단 거리
    P = [0] * (V + 1)  # 최단 경로 트리(부모 저장)
    Q = [s]
    D[s] = 0
    visit[s] = 1        # 시작점을 방문하고, 큐에 삽입
    while Q:            # 빈 큐가 아닐동안 반복
        v = Q.pop(0)
        for w in G[v]:  # v의 방문하지 않은 인접 정점 w을 찾는다.
            if not visit[w]:
                Q.append(w)
                visit[w] = 1;
                D[w] = D[v] + 1
                P[w] = v
    print(D[1:])

BFS1(1)


#=========================================
def BFS2(s):
    visit = [0] * (V + 1)
    Q = [s]
    visit[s] = 1        # 시작점을 방문하고, 큐에 삽입
    while Q:            # 빈 큐가 아닐동안 반복
        v = Q.pop(0)    # v의 방문하지 않은 인접 정점 w을 찾는다.
        for w in G[v]:
            if not visit[w]:
                Q.append(w)
                visit[w] = visit[v] + 1

    # s(출발)에서 g(도착) 까지의 거리 = visit[g] - 1
    print(visit[1:])

BFS2(1)





