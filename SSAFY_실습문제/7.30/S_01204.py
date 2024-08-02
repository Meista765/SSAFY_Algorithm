
T = int(input())

for test_case in range(1,T+1):
    test_number = int(input())
    scores = list(map(int,input().split()))

    arr = [0] * 101 # 점수의 카운트를 담을 리스트

    for i in range(len(scores)):
        arr[scores[i]] += 1

    max_val = 0 # 최빈 값 초기 값
    max_idx = 0 # 최빈 값 초기 인덱스
    for j in range(101):
        if max_val <= arr[j]:
            max_val = arr[j]
            max_idx = j
    print(f'#{test_case} {max_idx}')
