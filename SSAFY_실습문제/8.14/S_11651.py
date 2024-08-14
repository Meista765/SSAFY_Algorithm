import sys
sys.stdin = open('input.txt')
from collections import deque


def dfs(s,e):
    q = deque()
    q.append(s)
    visited[s] = 1

    while q:
        v = q.popleft()
        if v == e:
            return visited[v] - 1
        for w in G[v]:
            if not visited[w]:
                q.append(w)
                visited[w] = visited[v] + 1
    return 0





T = int(input())
for test_case in range(1,T+1):
    V, E = map(int,input().split())
    G = [[] for _ in range(V+1)]                # 인접 리스트
    for _ in range(E):
        u,v = map(int,input().split())
        G[u].append(v)
        G[v].append(u)
    S, E = map(int,input().split())
    visited = [0] * (V+1)

    result = dfs(S,E)
    print(f'#{test_case} {result}')
