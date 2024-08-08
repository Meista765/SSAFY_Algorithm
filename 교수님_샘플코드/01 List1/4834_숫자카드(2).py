import sys; sys.stdin = open('4834.txt')

#=======================================
# 정수로 저장해서 처리
for tc in range(1, int(input()) + 1):
    N = int(input())
    num = int(input())
    cnt = [0] * 10
    for _ in range(N):
        cnt[num % 10] += 1
        num //= 10

    max_idx = 0
    for i in range(1, 10):
        if cnt[max_idx] <= cnt[i]:
            max_idx = i
    print(max_idx, cnt[max_idx])
