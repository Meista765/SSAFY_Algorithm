import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for test_case in range(1,T+1):
    # 입력 받기
    N = int(input())
    A = [0] * N
    B = [0] * N 
    for i in range(N):
        A[i], B[i] = map(int,input().split())

    P = int(input())
    C = [0] * P
    for i in range(P):
        C[i] = int(input())

    arr = [0] * 5001 # 버스 정류장 수

    for i in range(N):
        for j in range(A[i],B[i]+1): # A[i] ~ B[i]
            arr[j] += 1
    print(f'#{test_case}', end = ' ')
    for k in range(P):
        print(arr[C[k]], end= ' ')
    print()
    

    


