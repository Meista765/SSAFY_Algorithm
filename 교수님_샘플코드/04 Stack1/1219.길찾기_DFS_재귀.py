import sys; sys.stdin = open('1219.txt', 'r')

for tc in range(1, 11):
    tc_num, E = map(int, input().split())
    arr = list(map(int, input().split()))

    G = [[] for _ in range(100)]  # 정점번호 0~99
    # 간선 정보를 읽자
    for i in range(0, E*2, 2):
        u, v = arr[i], arr[i+1]  # u -> v
        G[u].append(v)           # 유향그래프에 주의

    visited = [0] * 100

    def DFS(v):             # v: 현재 방문할 정점
        visited[v] = 1
        for w in G[v]:
            if not visited[w]:
                DFS(w)
    DFS(0)
    print(visited[99])

    # 재귀호출의 반환값으로 출력하기
    # def DFS(v):             # v: 현재 방문할 정점
    #     visited[v] = 1
    #     if v == 99:
    #         return 1
    #     for w in G[v]:
    #         if not visited[w]:
    #             if DFS(w):   # 1이 반환되면 종료
    #                 return 1
    #     return 0
    # print(DFS(0))

