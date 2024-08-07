# import sys
# sys.stdin = open('input.txt')

# 재귀
def dfs_2(v):
    global end
    visited[v] = True
    if v == end:
        return 1

    for w in G[v]:
        if not visited[w]:      # 방문하지 않은 노드라면
            if dfs_2(w):          # 재귀결과가 1이면 함수 종료
                return 1
    return 0                    # 실패

# 스택
def dfs_1(s):
    global end
    stack = [s]
    visited[s] =True
    v = s

    while stack:                # 스택이 비어있을 때 까지
        for w in G[v]:
            if w == end:        # 도착지점을 찾으면 return
                return 1
            if not visited[w]:  # 도착지점은 아니지만 방문하지 않은 지점이면
                stack.append(v)
                v = w           # 다음 방문 할 곳
                visited[w] = True
                break
        else:
            v = stack.pop()
    return 0

T = int(input())

for test_case in range(1,T+1):
    V, E = map(int,input().split()) # 노드의수, 엣지의 수
    G = [[] for _ in range(V+1)]    # 인접노드
    visited = [False] * (V+1)

    # 인접 리스트 만들기
    for _ in range(E):
        u,v = map(int,input().split())
        G[u].append(v)


    start, end = map(int,input().split()) # 출발지점, 끝지점
    result = dfs(start)

    print(f'#{test_case} {result}')
