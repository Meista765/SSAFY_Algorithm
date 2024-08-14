from collections import deque
import sys
sys.stdin = open('input.txt')

# 그래프는 0~101

def bfs(s):
    q = deque()
    q.append(s)
    visited[s] = 1

    while q:
        v = q.popleft()
        for w in G[v]:
            if not visited[w]:
                q.append(w)
                visited[w] = visited[v] + 1


for test_case in range(1,11):
    E, start = map(int,input().split())
    arr = list(map(int,input().split()))
    G = [[] for _ in range(101)]
    visited = [0] * 101

    for i in range(0,E,2):
        u,v = arr[i], arr[i+1]
        G[u].append(v)

    bfs(start)
    last_call = 0
    idx = 0
    for i in range(101):
        if last_call <= visited[i]:
             last_call = visited[i]
             idx = i
    print(f'#{test_case} {idx}')



