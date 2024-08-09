import sys
sys.stdin = open('input.txt')

def perm(k,N):
    S = 0       # sum
    global min_sum
    if k == N:
        for o in order:
            for i in range(N):
                S += arr[i][o]
        if min_sum > S:
            min_sum = S

    else:
        for i in range(N):
            if visited[i]:
                continue
            order[k] = my_list[i]
            visited[i] = k
            perm(k+1,N)
            visited[i] = 0
    return min_sum



T = int(input())
for test_case in range(1,T+1):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]
    my_list = list(range(N))
    visited = [0] * N
    order = [0] * N
    min_sum = float('inf')

    result = perm(0,N)
    print(result)