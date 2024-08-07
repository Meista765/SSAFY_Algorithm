import sys
sys.stdin = open('input.txt')


def dfs(s):
    global end
    stack = [s]
    visited[s] = 1
    v = s
    
    while stack:
        for w in G[v]:
            if w == end:
                return 1
            if not visited[w]: 
                stack.append(w)
                v = w
                visited[v] = 1
                break
        else:
            v = stack.pop()
    return 0


for _ in range(1,11):
    
    tc, E = map(int,input().split())
    arr = list(map(int,input().split()))
    G = [[] for _ in range(100)]        # 인접리스트
    visited = [0] * 100                 # 방문리스트
    
    start = 0                           # 출발 지점       
    end = 99                            # 도착 지점

    for i in range(E):
        u, v = arr[i*2], arr[i*2+1]
        G[u].append(v)

    result = dfs(1)
    print(f'#{tc} {result}')


