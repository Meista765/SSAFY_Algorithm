import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for test_case in range(1,T+1):
    N = int(input()) #카드의 장수
    card = input()
    arr = [0] * 10

    for i in range(N):
        arr[int(card[i])] += 1
    max_card = arr[0] #초기값 설정
    max_idx = 0
    for j in range(1,10):

        if max_card <= arr[j]:
            max_card = arr[j]
            max_idx = j
    print(f'#{test_case} {max_idx} {max_card}')