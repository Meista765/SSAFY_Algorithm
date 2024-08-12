import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline


def dfs(s,depth):
    global flag,visited
    visited[s] = 1
    if depth == 5:
        flag = True
        return 

        
    for w in G[s]:
        if not visited[w]:      #방문하지 않은 곳이면
            dfs(w,depth+1)
    visited[s] = 0 
        
            

N, E = map(int,input().split()) # N: 노드의 갯수, E: 엣지의 갯수
G = [[] for _ in range(N+1)] # 관계 리스트
visited = [0] * (N+1)        # 방문 리스트
flag = False
for _ in range(E):
    u, v = map(int,input().split())
    G[u].append(v)
    G[v].append(u)



for j in range(E):
    dfs(j,1)
    if flag:
        break
if flag:
    print(1)
else:
    print(0)







