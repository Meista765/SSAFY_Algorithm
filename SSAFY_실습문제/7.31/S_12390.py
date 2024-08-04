# import sys
# sys.stdin = open('input.txt','r')
T = int(input())
for test_case in range(1,T+1):
    N, K = map(int,input().split())

    arr = list(range(1,13))

    # 12-N
    cnt = 0
    

    for b in range(1<<12):
        sub_set =[] # 부분 집합의 합
        for i in range(12):
            if b & (1<<i):
                sub_set.append(arr[i])
        if len(sub_set) == N and sum(sub_set)==K:
            cnt +=1
            
    print(f'{test_case} {cnt}')