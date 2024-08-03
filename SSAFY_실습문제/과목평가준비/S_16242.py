import sys
sys.stdin = open('input.txt','r')

T = int(input())

for test_case in range(1,T+1):
    r,c,N,M = map(int,input().split())

    arr = [[0]*10 for _ in range(10)]
    num = 1 # 순회하면서 해당 인덱스에 넣어줄 값
    for i in range(M):
        for j in range(N):
            arr[r+i][c+(j+(N-1-(2*j)) * (i%2))] = num
            num += 1
    print(f'#{test_case}')
    for k in range(10):
        print(*arr[k])
