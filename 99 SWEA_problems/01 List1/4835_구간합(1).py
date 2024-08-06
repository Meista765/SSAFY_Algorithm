import sys; sys.stdin = open('4835.txt')



# 1차 배열의 연속적인 구간의 요소들을 순회
# 구간의 표현 => (시작인덱스, 끝 인덱스) => range(시작, 끝 + 1)
#           => (시작인덱스, 길이(개수)) => range(시작, 시작 + 길이)
# lst = [i for i in range(1, 11)]
# (2, 7)
# s, e = 2, 7
# for i in range(s, e + 1):
#     print(lst[i])
# s, l = 2, 4
# for i in range(s, s + l):
#     print(lst[i])

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    lst = list(map(int, input().split()))
    max_val = 0
    min_val = 1000000
    # 모든 구간의 시작 위치를 생성
    for s in range(N - M + 1):
        # 구간(시작=s, 길이=M)인 구간을 순회
        SUM = 0
        for i in range(s, s + M):
            SUM += lst[i]

        if max_val < SUM:
            max_val = SUM
        if min_val > SUM:
            min_val = SUM
    print(f'#{tc} {max_val - min_val}')
