# import sys
# sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    card = input().split()
    deck = [0]*N

    mid = (N+1)//2     # 아래 카드 시작, N//2+N%2

    for i in range(mid):
        if mid + i < N:
            deck[i*2] = card[i]
            deck[i*2+1] = card[i+mid]

        if i == mid-1: # 홀수 일 때 나머지 카드
            deck[i*2] = card[i]
    print(f'#{tc}', *deck)