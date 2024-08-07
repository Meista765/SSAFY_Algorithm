import sys
input = sys.stdin.readline

def DFS(arr,s,visited):
    stack = [s]
    visited[s] = True
    v = s
    
    while stack:                    # 스택이 빌때까지
        for w in arr[v]:
            if not visited[w]:      # 방문한 적 없는 노드이면
                stack.append(v)
                v = w
                visited[w] = True
                break
        else:
            v = stack.pop()

node, edge = map(int,input().split()) # node의 수, edge의 수

arr = [[] for _ in range(node+1)]     # 인접리스트
visited = [False] * (node+1)          # 방문리스트
for _ in range(edge):                 # 인접리스트 만들기
    u, v = map(int,input().split())
    arr[u].append(v)
    arr[v].append(u)


    
cnt = 0
for s in range(1,node+1):
    if not visited[s]:      #만약 방문한 적 없는 노드면 DFS실행
        DFS(arr,s,visited)
        cnt += 1

print(cnt)








