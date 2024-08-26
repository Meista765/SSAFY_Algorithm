import sys
input = sys.stdin.readline

N, M = map(int, input().split())

cards = list(map(int, input().split()))

def cards_sum():
    sum_list = []
    # 3장 찾기(비효율적 ㅜㅜ)
    for i in range(N-2):
        for j in range(i+1, N-1):
            for k in range(j+1, N):
                sum_value = cards[i] + cards[j] + cards[k]
                if sum_value <= M:
                    sum_list.append(sum_value)
    
    return max(sum_list)

print(cards_sum())