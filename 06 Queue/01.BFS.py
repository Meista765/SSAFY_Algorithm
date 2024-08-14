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
#=========================================
# 강의 코드

'''
7 8
4 2 1 2 1 3 5 2 4 6 5 6 6 7 3 7
'''

def bfs(s, V):  # 시작정점 s, 마지막 정점 V
    visited = [0] * (V+1)   # visited 생성
    q = []          # 큐 생성
    q.append(s)     # 시작점 인큐
    visited[s] = 1  # 시작점 방문표시
    while q:        # 큐에 정점이 남아있으면 front != rear
        t = q.pop(0)    # 디큐
        print(t)        # 방문한 정점에서 할일
        for w in adj_l[t]:  # 인접한 정점 중 인큐되지 않은 정점 w가 있으면
            if visited[w]==0:
                q.append(w)     # w인큐, 인큐되었음을 표시
                visited[w] = visited[t] + 1     # 몇 번 내려갔는지 확인할 수 있음
                print(visited)

V, E = map(int, input().split()) # 1번부터 V번 정점, E개의 간선
arr = list(map(int, input().split()))
# 인접리스트 -------------------------
adj_l = [[] for _ in range(V+1)]
for i in range(E):
    v1, v2 = arr[i*2], arr[i*2+1]
    adj_l[v1].append(v2)
    adj_l[v2].append(v1)    # 방향이 없는 경우
# 여기까지 인접리스트 -----------------
bfs(1, 7)



