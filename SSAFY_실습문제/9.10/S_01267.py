import sys
sys.stdin = open('input.txt')
from collections import deque
def bfs(start):
    q = deque(start)

    while q:
        v = q.popleft()
        print(v, end = ' ')
        for w in G[v]:
            degree[w] -= 1
            if degree[w] == 0:
                q.append(w)

for test_case in range(1,11):
    V, E = map(int,input().split())
    arr = list(map(int,input().split()))
    G = [[] for i in range(V+1)]     # 인접리스트
    degree = [0] * (V+1)                # 진입차수


    for i in range(E):
        u, v = arr[i*2], arr[i*2+1]
        G[u].append(v)
        degree[v] += 1

    # 시작 위치 찾기
    start = []
    for i in range(1,V+1):
        if not degree[i]:
            start.append(i)
    # print(G)
    # print(degree)
    print(f'#{test_case}', end = ' ')
    bfs(start)
    print()

