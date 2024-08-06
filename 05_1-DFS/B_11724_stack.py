# 연결 요소의 개수 (스택 구현)

import sys
#input = sys.stdin.readline
sys.stdin = open("C:/Users/82108/Downloads/sample_input.txt", "r")

n_node, n_edge = map(int, input().split())   # 노드 개수, 엣지 개수 받기
adj_list = [[] for _ in range(n_node+1)]     # 인접 리스트 초기화
visited = [False] * (n_node+1)               # 방문 리스트 초기화

def DFS(v):
    stack = [v]
    visited[v] = True
    
    while stack:
        pop_v = stack.pop()
        for x in adj_list[pop_v]:
            if not visited[x]: 
                stack.append(x)
                visited[x] = True


# 인접 리스트 만들기
for _ in range(n_edge):
    n1, n2 = map(int, input().split())
    adj_list[n1].append(n2)
    adj_list[n2].append(n1)

count = 0
for i in range(1, n_node+1):
    if not visited[i]:
        count += 1
        DFS(i)

print(count)