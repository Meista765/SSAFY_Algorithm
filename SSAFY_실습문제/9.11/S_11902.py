import sys
sys.stdin = open('input.txt')
from heapq import heappop, heappush

def dijkstra(s):
    visited = [0] * (N+1)
    D[s] = 0
    hq = [(0,s)]
    cnt = N+1

    while cnt and hq:
        w, u = heappop(hq)

        if visited[u]:          # 방문한 곳이면 이미 최단 경로이기 때문에 건너뜀
            continue
        visited[u] = 1
        for v,w in G[u]:
            if not visited[v] and D[v] > D[u] + w:
                D[v] = D[u] + w
                heappush(hq, (D[v], v))
        cnt -= 1

T = int(input())
for test_case in range(1,T+1):
    N, E = map(int,input().split())      # N: 마지막 연결점, E: 간선의 수
    G = [[] for _ in range(N+1)]         # 인접그래프

    for _ in range(E):
        u, v, weight = map(int,input().split())
        G[u].append((v,weight))

    D = [float('inf')] * (N + 1)  # 거리 정보 리스트

    dijkstra(0)
    print(f'#{test_case } {D[N]}')




