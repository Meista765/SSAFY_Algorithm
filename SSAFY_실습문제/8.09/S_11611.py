
def perm(k,N):
    S = 0                       # sum
    current_sum = 0 
    global min_sum
    
    #가지치기
    for i in range(k):
        current_sum += arr[i][order[i]]
    if current_sum > min_sum:
        return 
        
    
    if k == N:
        min_sum = current_sum

    else:
        for i in range(N):
            if visited[i]:
                continue
            order[k] = my_list[i]
            visited[i] = 1
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

    
    perm(0,N)
    print(f'#{test_case} {min_sum}')