# 친구 관계 파악하기

import sys
sys.setrecursionlimit(10000)
#input = sys.stdin.readline
sys.stdin = open("C:/Users/82108/Downloads/sample_input.txt", "r")

n_node, n_edge = map(int, input().split())   # 노드의 수, 엣지의 수
adj_list = [[] for _ in range(n_node)]       # 인접 리스트: 노드는 0부터 n_node-1까지
visited = [False] * n_node                   # 방문 리스트
arrive = False                               # 깊이 5에 도착했는지 여부 확인 변수

def DFS(node, depth):
    global arrive
    if depth == 5:  # 깊이가 5에 도달하면 True 반환 (재귀 종료)
        arrive = True
        return
    
    # 깊이가 5에 도달하지 못한 경우
    visited[node] = True
    for i in adj_list[node]:
        if not visited[i]:
            DFS(i, depth+1)  # 함수 호출되면 깊이 1 증가

    # 깊이 5에 도달하지 못하고 재귀가 돌아오면 모든 위치 방문 기록 False
    visited[node] = False
    
    
# 인접 리스트 채우기
for _ in range(n_edge):
    n1, n2 = map(int, input().split())
    adj_list[n1].append(n2)
    adj_list[n2].append(n1)
    
for i in range(n_node):
    DFS(i, 1)   # 노드, 깊이 파라미터로 주기
    if arrive:
        print(1)  
        break
else:
    print(0)