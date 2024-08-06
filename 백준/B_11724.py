import sys
input = sys.stdin.readline

def DFS(arr,v,visited):
    stack= [v]
    visited[v] = True
    
    
    while stack:                    # 스택이 빌때까지
        for i in arr[stack.pop()]:
            if not visited[i]:      # 방문한 적 없는 노드이면
                stack.append(i)
                visited[i] = True


node, edge = map(int,input().split()) # node의 수, edge의 수

arr = [[] for _ in range(node+1)]     # 인접리스트
visited = [False] * (node+1)              # 방문리스트
for _ in range(edge):                 # 인접리스트 만들기
    u, v = map(int,input().split())
    arr[u].append(v)
    arr[v].append(u)


    
cnt = 0
for i in range(1,node+1):
    if not visited[i]:      #만약 방문한 적 없는 노드면 DFS실행
        DFS(arr,i,visited)
        cnt += 1
print(cnt)







