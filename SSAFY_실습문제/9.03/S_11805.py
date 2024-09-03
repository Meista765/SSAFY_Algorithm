import sys
sys.stdin = open('input.txt')

T = int(input())
for test_case in range(1,T+1):
    N = int(input())
    time = []
    for _ in range(N):
        time.append(list(map(int,input().split())))

    # 정렬
    time.sort(key=lambda x: (x[1], x[0]))

    cnt = 0
    e = -1
    for t in time:
        if t[0] >= e:
            cnt += 1
            e = t[1]

    print(f'#{test_case} {cnt}')
