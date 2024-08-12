from collections import deque
import sys
input = sys.stdin.readline

def DFS(s):
    print(s, end = ' ')
    visited[s] = 1              # 방문리스트 체크
    for w in G[s]:
        if not visited[w]:      # 방문하지 않은 노드이면
            DFS(w)

def BFS(s):
    q = deque()                 # 큐 생성
    q.append(s)
    visited[s] = 1
    while q:                    # 큐가 빌 때까지
        v = q.popleft()
        print(v, end = ' ')
        for w in G[v]:
            if not visited[w]:
                visited[w] = 1
                q.append(w)

N, E, S = map(int,input().split())  # N: 노드 개수, E: 에지 개수, S: 시작점
G = [[] for _ in range(N+1)]        # 인접 리스트
visited = [0] * (N+1)               # 방문 리스트

# 인접 리스트 만들기
for _ in range(E):
    u,v = map(int,input().split())
    G[u].append(v)
    G[v].append(u)

# 정렬
for i in range(N+1):
    G[i].sort()

DFS(S)
print()
visited = [0] * (N+1)               # 방문 리스트 초기화
BFS(S)

