import sys
sys.stdin = open('input.txt')
T = int(input())

for test_case in range(1,T+1):
    N = int(input())
    start = [0] * N # 출발 방
    end = [0] * N   # 도착 방
    cnt_list = [0] * 201 # 지나온 것 체크

    for i in range(N):
        start[i], end[i] = map(int,input().split())

    for i in range(N):
        if start[i] < end[i]:    # 출발 방이 도착 방보다 작을경우
            s = (start[i]+1) // 2
            e = (end[i]+1) // 2
        else:                   # 출발 방이 도착 방보다 클경우
            e = (start[i]+1) // 2
            s = (end[i]+1) // 2

        for j in range(s,e+1):
            cnt_list[j] += 1

    answer = max(cnt_list)

    print(f'#{test_case} {answer}')



