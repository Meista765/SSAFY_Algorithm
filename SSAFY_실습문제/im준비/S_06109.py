
T= int(input())
for test_case in range(1,T+1):
    N, direction = input().split()
    N = int(N)
    arr = [list(map(int,input().split())) for _ in range(N)]
    result = [[] for _ in range(N)]
