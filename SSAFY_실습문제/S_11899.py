import sys
sys.stdin = open('input.txt')

def find(x):
    if x == p[x]:
        return x
    else:
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
    N, M = map(int,input().split())
    arr = list(map(int,input().split()))
    p = [i for i in range(N+1)]
    ans = N
    for i in range(M):
        u, v = arr[i*2], arr[i*2+1]
        union(u,v)

    print(f'#{test_case} {ans}')


