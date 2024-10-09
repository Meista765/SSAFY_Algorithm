import sys
sys.stdin = open('input.txt')
from collections import deque
from heapq import heappop,heappush

# 방향설정: 상우하좌
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

# 섬 라벨링 작업을 위한 BFS함수 설계
def BFS(i,j,label):
    q = deque()
    q.append((i,j))
    visited[i][j] = 1
    arr[i][j] = label

    while q:
        r, c = q.popleft()
        for k in range(4):
            nr = r + dr[k]
            nc = c + dc[k]

            if 0 <= nr < N and 0 <= nc < M and arr[nr][nc] != 0 and not visited[nr][nc]:
                arr[nr][nc] = label
                visited[nr][nc] = 1
                q.append((nr,nc))

# 섬 간의 연결
def connect(n):
    q = deque()

    for i in range(N):
        for j in range(M):
            if arr[i][j] == n:
                q.append((i,j))

    while q:
        v = q.popleft()
        for k in range(4):
            length = 0
            nr = v[0]
            nc = v[1]
            while True:
                nr += dr[k]
                nc += dc[k]
                if nr < 0 or nr >= N or nc < 0 or nc >= M or arr[nr][nc] == n:          # 범위를 벗어나거나 같은 섬이면 종료
                    break
                else:
                    if arr[nr][nc] != 0:                                                # 다른 섬을 만났을 때
                        if length > 1:                                                  # 다리의 길이가 1보다 크면
                            edges.add((n,arr[nr][nc],length))                           # 간선(edges)정보에 저장
                            break
                        else:
                            break
                    length += 1


N, M = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(N)]


# 섬 라벨링 작업
label = 1
visited = [[0] * M for _ in range(N)]                   # 방문정보 체크
for i in range(N):
    for j in range(M):
        if arr[i][j] == 1 and not visited[i][j]:
            BFS(i,j,label)
            label += 1          # 최종 label: 5

# 섬 라벨링 작업 결과물 출력
# for i in range(N):
#     print(*arr[i])



# 섬 연결 작업
edges = set()
for n in range(1,label+1):
    connect(n)
edges = sorted(list(edges))
# print(edges)

# 그래프 형식으로 저장
G = [[] for _ in range(label)]
for u,v,w in edges:
    G[u].append((v,w))

# print(G)

# MST-PRIM
p = [i for i in range(label)]     # 간선 정보 저장(어디서 연결 됐는지)
key = [float('inf')] * label
key[1] = 0
mst = [0] * label
hq = [(0,1)]

cnt = label - 1

while cnt and hq:

    val, u = heappop(hq)

    if mst[u]:              # 이미 확정됐으면
        continue
    mst[u] = 1

    for v, weight in G[u]:
        if not mst[v] and key[v] > weight:
            p[v] = u
            key[v] = weight
            heappush(hq,(key[v],v))
    cnt = -1

# print(key)
# print(p)
# print(sum(key[1:]))

answer = sum(key[1:])
if answer == float('inf'):
    print(-1)
else:
    print(answer)







