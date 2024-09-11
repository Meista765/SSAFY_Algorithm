import sys
sys.stdin = open('input.txt')
from heapq import heappop, heappush

def prim(s):
    key[s] = 0                  # 초기 설정
    hq = [(key[s],s)]           # weight, 시작 노드
    cnt = N + 1
    sum_weight = 0
    while cnt:
        weight, v = heappop(hq)

        # 방문한 노드인지 체크
        if visited[v]:
            continue

        # 방문하지 않은 노드이면 방문체크
        visited[v] = 1
        sum_weight += weight

        # 갈 수 있는 노드 확인
        for w,weight in G[v]:
            if not visited[w] and key[w] > weight:      # 방문하지 않은 노드이면
                key[w] = weight
                p[w] = v
                heappush(hq,(key[w],w))
        cnt -= 1
    return sum_weight

T = int(input())
for test_case in range(1,T+1):
    N, E = map(int,input().split())            # N = 마지막 노드 번호, E = 간선의 수
    G = [[] for _ in range(N+1)]                # 인접리스트

    for _ in range(E):
        u, v, w = map(int,input().split())
        G[u].append((v,w))
        G[v].append((u,w))

    p = [i for i in range(N+1)]                 # 간선 정보
    key = [float('inf')] * (N+1)
    visited = [0] * (N+1)                       # 방문 정보

    result = prim(0)
    print(f'#{test_case} {result}')