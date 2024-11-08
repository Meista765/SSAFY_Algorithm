import sys
sys.stdin = open('sample_input.txt', 'r')
from collections import deque

# bfs
def bfs():
    pass

for tc in range(1, 11):
    V, E = map(int, input().split())

    graph = [[0, []] for _ in range(V + 1)] # 진입 차수, 자식 노드 리스트

    edges = list(map(int, input().split()))

    for i in range(2 * E):
        if i % 2 == 0:  # 부모 노드일 때
            graph[edges[i]][1].append(edges[i + 1]) # 해당 노드의 자식 저장
        else:           # 자식 노드일 때
            graph[edges[i]][0] += 1                 # 진입 차수 올려주기

    