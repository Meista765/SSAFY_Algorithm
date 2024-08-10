def comb(k,n,cnt_1,current_sum):
    global cnt
    
    # 가지치기 
    if current_sum > K:     # 현재까지의 합이 K보다 크면 함수 종료
        return 
    if cnt_1 > N:				# 부분 집합의 원소의 수가 N보다 크면 함수 종료
        return 

    if k == n:
        if cnt_1 == N and current_sum == K:
            cnt += 1
       
    else:
        comb(k+1,n,cnt_1,current_sum) 
        comb(k+1,n,cnt_1+1,current_sum+arr[k])               # cnt_1: 1의 갯수



T = int(input())
for test_case in range(1,T+1):
    M = 12
    N, K = map(int,input().split())     # N: 부분집합의 원소의 수 K: 원소의 합
    arr = list(range(1,M+1))            # 1~12까지의 리스트
    cnt = 0                             # 문제에서 요구하는 조건의 갯수
    comb(0,12,0,0)
    print(f'#{test_case} {cnt}')