############# DFS 재귀호출 #############


## 교안 연습문제 방문 순서

'''
1
7 8
1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7
'''

def dfs(v):
    visited[v] = 1
    print(v, end = ' ')

    for w in G[v]:
        if not visited[w]:
            dfs(w)