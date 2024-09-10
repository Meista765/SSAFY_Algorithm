import sys
sys.stdin = open('input.txt')

def find(x):
    if p[x] == x:
        return x

    p[x] = find(p[x])
    return p[x]

def union(x,y):
    global ans
    a = find(x)
    b = find(y)
    if a == b:
        return
    p[b] = a
    ans -= 1
T = int(input())
for test_case in range(1,T+1):
    V, E = map(int,input().split())
    p = [i for i in range(V+1)]
    ans = V

    for _ in range(E):
        u, v = map(int,input().split())
        union(u,v)

    print(f'#{test_case} {ans}')



