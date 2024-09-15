import sys
sys.stdin = open('input.txt')
from heapq import heappush,heappop

# x번 정점에서 각 정점으로 가는 최단 거리를 구할 함수
def dijkstra(s):
    visited = [0] * (N+1)               # 최소 비용을 계산한 정점을 체크할 리스트
    D[s] = 0
    hq = [(0, s)]

    cnt = N
    while cnt and hq:
        weight, w = heappop(hq)

        # 방문한 곳인지 확인
        if visited[w]:
            continue

        visited[w] = 1

        for v,weight in G[w]:
            if not visited[v] and D[v] > D[w] + weight:
                D[v] = D[w] + weight
                heappush(hq, (D[v], v))
        cnt -= 1

# 각 정점에서 x번 정점으로 가는 최단 거리를 구할 함수
def dijkstra_2(s):
    visited = [0] * (N + 1)  # 최소 비용을 계산한 정점을 체크할 리스트
    D_go = [(float('inf'))] * (N + 1)  # 각 정점에서 1번으로 가는 최단 거리
    D_go[s] = 0
    hq = [(0, s)]


    while hq:
        weight, w = heappop(hq)

        if w == X:  # 도착지에 도착했다면
            return weight

        if visited[w]:
            continue

        visited[w] = 1

        for v,weight in G[w]:
            if not visited[v] and D_go[v] > D_go[w] + weight:
                D_go[v] = D_go[w] + weight
                heappush(hq, (D_go[v], v))




T = int(input())
for test_case in range(1,T+1):
    N, M, X = map(int,input().split())  # N: 정점의 수, M: 간선의 수 X: 인수의 집
    G = [[] for _ in range(N+1)]        # 인접리스트 생성

    # 인접리스트 생성(단방향)
    for _ in range(M):
        x, y, c = map(int,input().split())
        G[x].append((y,c))

    D = [(float('inf'))] * (N+1)        # X번에서 각 정점으로 가는 최단 거리


    max_val = float('-inf')

    dijkstra(X)
    # print(D)
    for i in range(1,N+1):
        go = dijkstra_2(i)
        # print(go)
        total_weight = D[i] + go
        if max_val < total_weight:
            max_val = total_weight

    print(f'#{test_case} {max_val}')







