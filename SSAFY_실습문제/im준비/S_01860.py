import sys
sys.stdin = open('input.txt')

T = int(input())

for test_case in range(1,T+1):
    N, M, K = map(int,input().split())      # N = 예약자 수, M초의 시간을 들이면 K개의 붕어빵
    arr = list(map(int,input().split()))    # 손님들 오는 시간

    # 손님들 오는 시간 정렬
    arr.sort()

    last = arr[-1]              # 가장 마지막에 오는 손님의 시간
    cnt_list = [0] * (last+1)   # 붕어빵 갯수
    answer = 'Possible'

    # 초기 cnt_list 세팅
    for i in range(N):
        cnt_list[arr[i]] -= 1


    for i in range(1,last+1):
        cnt_list[i] += cnt_list[i-1]
        if i % M == 0:
            cnt_list[i] += K


    for j in range(0,last+1):
        if cnt_list[j] < 0:
            answer = 'Impossible'

    print(f'#{test_case} {answer}')







