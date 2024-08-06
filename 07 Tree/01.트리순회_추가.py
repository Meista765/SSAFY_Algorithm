import sys; sys.stdin = open('tree_input.txt')
V, E = map(int, input().split())
L = [0] * (V + 1)
R = [0] * (V + 1)
P = [0] * (V + 1)

arr = list(map(int, input().split()))
for i in range(0, E * 2, 2):
    p, c = arr[i], arr[i + 1]
    # p(부모)를 인덱스로 사용
    if L[p] == 0: L[p] = c
    else: R[p] = c
    P[c] = p

# 트리의 높이를 계산.
# 1이 루트인 트리의 높이 --> 4, 3이 루트인 트리의 높이 --> 3
def tree_height(v):
    pass
    if v == 0: return -1
    lh = tree_height(L[v])
    rh = tree_height(R[v])
    return max(lh, rh) + 1

print(tree_height(1)) # --> 4를 계산
print(tree_height(3)) # --> 3을 계산

# 높이가 3인 노드들 찾기 = (7, 8, 9, 10, 11)

# 3번 노드가 루트인 트리의 전체 노드수 = 8
cnt = 0
def tree_size(v):
    if v == 0: return 0
    l = tree_size(L[v])
    r = tree_size(R[v])
    return l + r + 1

print(tree_size(3)) # ==> 8 출력
print(tree_size(1)) # ==> 13 출력

# 8번 노드와 10번 노드의 공통조상 = (1, 3)
def find_common_ancestor(v1, v2):
    pass
find_common_ancestor(1, 3) # ==> 1, 3 출력 또는 결과를 반환

