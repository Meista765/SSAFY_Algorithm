# 연결 요소의 개수 (재귀 구현)

import sys
sys.setrecursionlimit(10000)
#input = sys.stdin.readline
sys.stdin = open("C:/Users/82108/Downloads/sample_input.txt", "r")

n_node, n_edge = map(int, input().split())   # 노드 개수, 엣지 개수 받기
adj_list = [[] for _ in range(n_node+1)]     # 인접 리스트 초기화
visited = [False] * (n_node+1)               # 방문 리스트 초기화

# DFS 함수
def DFS(v):
    global adj_list
    visited[v] = True
    # 전부 방문했으면 for문 내에 if문으로 들어가지 않기 때문에 재귀가 종료됨
    for i in adj_list[v]:
        if not visited[i]:   # 방문 한 적이 없으면
            DFS(i)           # 거기로 가서 다시 인접 리스트 내 노드 조사

# 인접 리스트 채우기
for _ in range(n_edge):
    n1, n2 = map(int, input().split())   # 엣지로 연결된 숫자 2개 받기
    # 인접 리스트에 추가
    adj_list[n1].append(n2)
    adj_list[n2].append(n1)

count = 0   # 연결 요소 개수
for i in range(1, n_node+1):
    if not visited[i]:
        count += 1
        DFS(i)

print(count)