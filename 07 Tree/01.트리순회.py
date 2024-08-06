import sys; sys.stdin = open('tree_input.txt')

V, E = map(int, input().split())
L = [0] * (V + 1)
R = [0] * (V + 1)
P = [0] * (V + 1)

arr = list(map(int, input().split()))

for i in range(0, E * 2, 2):
    p, c = arr[i], arr[i + 1]
    # p(부모)를 인덱스로 사용
    if L[p] == 0:
        L[p] = c
    else:
        R[p] = c
    P[c] = p

def inorder(v):
    if v == 0: return
    print(v, end=' ')
    inorder(L[v])
    print(v, end=' ')
    inorder(R[v])
    print(v, end=' ')

inorder(1)


#======================================
# 너비 우선 탐색
print()
def bfs(s):
    Q = [s]
    while Q:
        v = Q.pop(0)
        if v == 0:
            continue
        else:
            print(v, end=' ')
            Q.append(L[v])
            Q.append(R[v])
bfs(1)





