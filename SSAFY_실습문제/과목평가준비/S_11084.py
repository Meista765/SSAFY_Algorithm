import sys
sys.stdin = open('input.txt','r')


T = int(input())

for test_case in range(1,T+1):
    N = int(input()) # 양수의 갯수
    arr = list(map(int,input().split()))

    max_idx = 0
    min_idx = 0
    max_val = arr[0]
    min_val = arr[0]
    for i in range(N):
        
        # 최대 값 위치 찾기
        if max_val <= arr[i]:
            max_val = arr[i]
            max_idx = i

        # 최소 값 위치 찾기
        if min_val > arr[i]:
            min_val = arr[i]
            min_idx = i 
    
    if max_idx > min_idx:
        print(f'#{test_case} {max_idx-min_idx}')

    else:
        print(f'#{test_case} {min_idx - max_idx}')
