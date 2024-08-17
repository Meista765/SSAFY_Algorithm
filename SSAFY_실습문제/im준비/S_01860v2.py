import sys
sys.stdin = open('input.txt')
T = int(input())

for test_case in range(1,T+1):
    N, M, K = map(int,input().split())
    guest = list(map(int,input().split()))
    guest.sort()
    answer = 'Possible'
    cur_time = 0 # 현재 시각
    cur_cnt = 0  # 현재 남은 붕어 빵의 수
    for i in range(N):
        while cur_time < guest[i]:
            cur_time += 1
            if cur_time % M == 0:   # 붕어빵이 완성되는 시간이면
                cur_cnt += K
        if cur_time == guest[i]:    # 손님이 도착했을 때
            if cur_cnt < 1:
                answer = 'Impossible'
                break
            else:
                cur_cnt -= 1

    print(f'#{test_case} {answer}')



