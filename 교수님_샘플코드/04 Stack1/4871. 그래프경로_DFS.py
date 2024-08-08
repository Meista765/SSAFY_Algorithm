import sys; sys.stdin = open('4871.txt', 'r')

T = int(input())
for tc in range(1, T + 1):
    V, E = map(int, input().split())
    G = [[] for _ in range(V + 1)]

    for _ in range(E):
        u, v = map(int, input().split())
        G[u].append(v)      # 유향 그래프

    v, goal = map(int, input().split())

    S = []
    visited = [0] * (V + 1)
    visited[v] = 1

    while True:
        for w in G[v]:
            if not visited[w]:
                S.append(v)
                visited[w] = 1
                v = w
                break
        else:
            if not S: break
            v = S.pop()

    print(f'#{tc} {visited[goal]}')
