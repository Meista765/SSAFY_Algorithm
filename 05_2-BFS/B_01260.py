# # DFS와 BFS 프로그램
import sys
#input = sys.stdin.readline
sys.stdin = open("C:/Users/82108/Downloads/sample_input.txt", "r")

from collections import deque

def DFS(v):
    global visited, path
    
    visited[v] = 1            # 현재 노드 방문 표시
    path.append(v)            # 탐색 경로에 현재 노드 추가
    
    for i in adj_l[v]:        # 현재 정점과 인접한 정점들 순회
        if not visited[i]:    # 방문한적 없으면
            DFS(i)            # DFS 재귀 들어가자

def BFS(v):
    global visited, path
    
    queue = deque()         # 큐 만들기
    queue.appendleft(v)     # 시작 노드 enqueue
    visited[v] = 1          # 시작 노드 방문 표시
    
    while queue:            # 큐가 비어있을 때까지 반복
        x = queue.pop()         # dequeue      
        path.append(x)          # 탐색 경로에 dequeue한 노드 추가 
        for i in adj_l[x]:           # 현재 정점과 인접한 정점들 순회
            if not visited[i]:       # 방문한적 없으면
                queue.appendleft(i)  # enqueue
                visited[i] = 1       # enqueue한 노드 방문 표시

n_node, n_edge, start_v = map(int, input().split())   # 정점 개수, 간선 개수, 시작 정점 번호
adj_l = [[] for _ in range(n_node+1)]       # 인접 리스트
visited = [0] * (n_node+1)                  # 방문 리스트
path = []                                   # 탐색 경로

# 인접 리스트 채우기
for _ in range(n_edge):
    n1, n2 = map(int, input().split())
    adj_l[n1].append(n2)
    adj_l[n2].append(n1)
    
# 방문할 수 있는 정점이 여러 개인 경우에는 정점 번호가 작은 것을 먼저 방문해야하므로
for adj_nodes in adj_l:
    adj_nodes.sort()        # 각 노드의 인접 리스트 오름차순 정렬

DFS(start_v)    # DFS 호출
print(*path)     # 탐색 경로 출력

visited = [0] * (n_node+1)       # 방문 리스트 초기화
path = []                        # 탐색 경로 초기화

BFS(start_v)    # BFS 호출
print(*path)     # 탐색 경로 출력