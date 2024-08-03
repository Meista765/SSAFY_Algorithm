import sys
sys.stdin = open('input.txt','r')

T = int(input())

for test_case in range(1,T+1):
    # 입력받기
    N, Q = map(int,input().split())
    L = [0] * Q
    R = [0] * Q

    for i in range(Q):
        L[i],R[i] = map(int,input().split())
    
    arr = [0] * N

    for i in range(Q):
        for j in range(L[i],R[i]+1):
            arr[j-1] = i+1
    
    print(f'#{test_case}', *arr)

            

    

    
