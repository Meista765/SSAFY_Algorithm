import sys
sys.stdin = open('input.txt')
from collections import deque

def bfs(s):
    global cnt
    q = deque()
    q.append(s)
    visited[s] = 1

    while q:
        v = q.popleft()

        for w in G[v]:
            if not visited[w]:
                q.append(w)
                visited[w] = visited[v] + 1

T = int(input())
for test_case in range(1,T+1):
    N, M = map(int,input().split())
    G = [[] for _ in range(N+1)]        # 인접리스트
    visited = [0] * (N+1)

    # 인접리스트 생성
    for _ in range(M):
        u, v = map(int,input().split())
        G[u].append(v)
        G[v].append(u)
    cnt = 0
    bfs(1)
    for i in range(N+1):
        if visited[i] == 2 or visited[i] == 3:
            cnt += 1
    print(f'#{test_case} {cnt}')
