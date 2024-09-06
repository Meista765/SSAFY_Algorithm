import sys
sys.stdin = open('input.txt')

def backtrack(location, cur_cnt):   # location: 현재 위치
    global min_cnt
    # 가지치기
    if cur_cnt >= min_cnt:
        return

    if location >= N:
        min_cnt = cur_cnt
        return

    else:
        for i in range(1, arr[location]+1):
            backtrack(location+i, cur_cnt+1)



T = int(input())
for test_case in range(1,T+1):
    arr = list(map(int,input().split()))
    N = arr[0]                          # 정류장 수
    min_cnt = 101                           # 초기 값
    backtrack(1,0)
    print(f'#{test_case} {min_cnt-1}')  # 첫번째 충전지는 count에 미포함