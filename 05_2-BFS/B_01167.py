# 트리의 지름
import sys
#input = sys.stdin.readline
sys.stdin = open('C:/Users/SSAFY/Downloads/sample_input.txt', 'r')

from collections import deque

N = int(input())    # N: 노드 개수
adj_l = [[] for _ in range(N+1)]     # 인접 리스트

# 인접 리스트 채우기
for _ in range(N):
    s_node, *adj_nodes, _ = map(int, input().split())
    for i in range(0, len(adj_nodes), 2):
        adj_node = adj_nodes[i]     # 인접 노드
        dist = adj_nodes[i+1]       # 거리
        adj_l[s_node].append((adj_node, dist))    # (인접 노드, 거리) 형태로 기록

visited = [False] * (N+1)   # 방문 리스트 초기화
dist_list = [0] * (N+1)     # 거리 리스트 초기화


# BFS 구현
def BFS(s):     # s: 시작 노드
    global visited, dist_list

    queue = deque()             # 큐 생성
    queue.append(s)             # 시작 노드 넣고 시작
    visited[s] = True           # 시작 노드 방문 표시
    
    while queue:
        node = queue.popleft()     # 왼쪽 dequeue
        # dequeue 한 노드의 인접 노드 탐색
        for i, dist in adj_l[node]:         # i: 노드 번호, dist: 거리
            # 방문한적 없는 노드면 enqueue
            if not visited[i]:
                visited[node] = True          # enqueue할 노드 방문 기록
                queue.append(i)
                dist_list[i] = dist_list[node] + dist


BFS(1)   # 그냥 무조건 1부터 시작하자 (임의의 시작점)
max_dist = 0
max_node = 0
# 가장 거리가 먼 노드 찾기
for i in range(2, N+1):     # 1번 노드를 시작점으로 넣었으니 2부터 탐색
    if dist_list[i] > max_dist:
        max_dist = dist_list[i]
        max_node = i

visited = [False] * (N+1)   # 방문 리스트 초기화
dist_list = [0] * (N+1)     # 거리 리스트 초기화
BFS(max_node)               # 가장 거리가 멀었던 노드부터 시작
print(max(dist_list))       # 트리의 지름(최대 거리) 출력