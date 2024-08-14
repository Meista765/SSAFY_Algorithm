from collections import deque

def bfs(s):
    q = deque()
    q.append(s)
    visited[s] = 1           # 방문리스트 체크
    
    while q:
        v = q.popleft()
        for w in G[v]:
            if visited[w[0]] == 0:  # 방문하지 않은 곳이라면
                q.append(w[0])
                visited[w[0]] = 1
                distance[w[1]] = distance[v] + w[1]


N = int(input())
G = [[] for _ in range(N+1)]
visited = [0] * (N+1)
distance = [0] * (N+1)  #거리리스트

for _ in range(N):
    input_list = list(map(int,input().split()))
    idx = input_list[0]
    M = len(input_list)
    for i in range(1,M-1,2):
        G[idx].append((input_list[i],input_list[i+1]))
        
bfs(1)
max_idx = 1

for i in range(2,N+1):
    if distance[max_idx] < distance[i]:
        max_idx = i

distance = [0] * (N+1)
visited = [0] * (N+1)
bfs(max_idx)
distance.sort()
print(distance[N])