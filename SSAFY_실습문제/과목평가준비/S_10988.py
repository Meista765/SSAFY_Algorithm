import sys
sys.stdin = open('input.txt','r')


T = int(input())

for test_case in range(1,T+1):
    N, K = map(int,input().split()) # N = 정수의 수, K = K번째 작은수
    arr = list(map(int,input().split()))

    M = max(arr)

    count_list = [0] * (M+1)

    # 요소의 갯수 리스트에 담기
    for i in range(N):
        count_list[arr[i]] += 1

    # print(count_list) # 확인용
    cnt = K

    for j in range(M+1):
        if count_list[j] != 0:
            cnt -= 1
        if cnt == 0:
            break
    
    print(f'#{test_case} {j}')

        
        


