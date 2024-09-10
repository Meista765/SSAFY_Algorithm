import sys
sys.stdin = open('input.txt')
from collections import deque

def bfs(s):
    q = deque()
    q.append(s)
    visited = [0] * (N+1)
    cnt = 0
    while q:
        v = q.popleft()
        for w in G[v]:
            if not visited[w]:
                cnt += 1
                q.append(w)
                visited[w] = 1
    return cnt

def bfs_reverse(s):
    q = deque()
    q.append(s)
    visited = [0] * (N + 1)
    cnt = 0
    while q:
        v = q.popleft()
        for w in G_reverse[v]:
            if not visited[w]:
                cnt += 1
                q.append(w)
                visited[w] = 1
    return cnt



T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    M = int(input())
    G = [[] for _ in range(N+1)]
    G_reverse = [[] for _ in range(N+1)]

    for _ in range(M):
        u, v = map(int,input().split())
        G[u].append(v)
        G_reverse[v].append(u)
    ans = 0
    for i in range(1,N+1):
        original = bfs(i)
        reverse = bfs_reverse(i)
        if original + reverse == N-1:
            ans += 1

    print(f'#{test_case} {ans}')



