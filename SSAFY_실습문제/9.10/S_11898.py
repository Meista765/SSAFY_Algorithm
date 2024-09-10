'''
+1, -1, *2, -10
'''

import sys
sys.stdin = open('input.txt')
from collections import deque

def bfs(n):
    q = deque()
    q.append((n, 0))
    visited = [0] * 1000001
    visited[n] = 1
    while q:
        v, cnt = q.popleft()
        if v == M:
            return cnt
        else:
            for k in range(4):
                if k == 0:  # +1
                    if v+1 <= 1000000 and not visited[v+1]:
                        q.append((v+1, cnt + 1))
                        visited[v+1] = 1
                elif k == 1:
                    if v -1 <= 1000000 and not visited[v-1]:
                        q.append((v-1, cnt+1))
                        visited[v-1] = 1
                elif k == 2:
                    if v*2 <= 1000000 and not visited[v*2]:
                        q.append((v*2, cnt+1))
                        visited[v*2] = 1
                else:
                    if v - 10 <= 1000000 and not visited[v-10]:
                        q.append((v-10, cnt+1))
                        visited[v-10] = 1


T = int(input())
for test_case in range(1,T+1):
    N, M = map(int,input().split())
    result = bfs(N)
    print(f'#{test_case} {result}')
