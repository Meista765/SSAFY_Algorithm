N = 6

# 위에서부터 4 2 6 1 3 5로 연결된 트리
tree = [0, 4, 2, 6, 1, 3, 5]    # 노드 번호가 배열의 인덱스에 대응
# 1 ~ 6 이 저장된 완전이진트리 중위 탐색
def dfs(v):
    if v > N: return
    dfs(v*2) # 왼쪽자식
    print(tree[v], end = ' ')
    dfs(v*2 + 1) # 오른쪽자식
    
dfs(1)
# 1 2 3 4 5 6

print()

# 다른 방식
tree = [0] * (N + 1)
cnt = 1

def dfs2(v):
    global cnt
    if v > N: return
    
    dfs2(v*2)
    tree[v] = cnt
    cnt += 1
    dfs2(v*2 + 1)

dfs2(1)

print(tree[1:])