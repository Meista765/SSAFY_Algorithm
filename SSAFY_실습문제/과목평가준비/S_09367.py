import sys
sys.stdin = open('input.txt','r')
T = int(input())

for test_case in range(1,T+1):
    N = int(input())
    arr = list(map(int,input().split()))
    max_cnt =1
    cnt = 1

    for i in range(N-1):
        if arr[i] < arr[i+1]:
            cnt += 1
            
        else:
            if max_cnt < cnt:
                max_cnt = cnt 
                
            cnt = 1
        if max_cnt < cnt:
            max_cnt = cnt 
    
    print(f'#{test_case} {max_cnt}')
