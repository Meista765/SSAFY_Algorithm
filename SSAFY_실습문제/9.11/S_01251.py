'''
모든 섬에 대해서 어떤 섬에서 그 섬을 제외한 모든 섬을 연결할 때 뜨는 비용을 계산해서 리스트에 담아서 프림 알고리즘을 사용한다.
어떻게 하면 계산을 줄일까 고민중.....

'''

import sys
sys.stdin = open('input.txt')
from heapq import heappop,heappush

def prim(start):
    D[start] = 0
    hq = [(D[start],start)]
    cnt = N
    pay = 0

    while cnt:
        weight,v = heappop(hq)

        # 방문한 노드인지 체크
        if visited[v]:
            continue

        # 방문하지 않은 노드라면
        visited[v] = 1      # 방문체크
        pay += E * weight

        # 노드 확인
        for w,weight in G[v]:
            if not visited[w] and D[w] > weight:
                D[w] = weight
                p[w] = v
                heappush(hq,(D[w],w))
        cnt -= 1
    return pay


T = int(input())
for test_case in range(1,T+1):
    N = int(input())                    # 섬의 갯수
    X = list(map(int,input().split()))
    Y = list(map(int,input().split()))
    E = float(input())

    G = [[] for _ in range(N)]     # 인접리스트
    visited = [0] * N               # 방문 정보 리스트
    D = [(float('inf'))] * N      # 간선 정보
    p = [i for i in range(N)]

    # 인접리스트 생성
    for i in range(N-1):
        for j in range(i+1, N):
            distance = (X[i] - X[j]) ** 2 + (Y[i] - Y[j]) ** 2
            G[i].append((j, distance))
            G[j].append((i, distance))

    result = round(prim(0))
    print(f'#{test_case} {result}')
