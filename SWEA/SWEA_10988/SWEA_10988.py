# 선택 정렬
T = int(input())

for tc in range(1, T + 1):
    N, K = map(int, input().split())
    
    number_list = list(map(int, input().split()))
    
    # 선택 정렬
    for i in range(N - 1):
        min_idx = i
        for j in range(i + 1, N):
            if number_list[j] < number_list[min_idx]:
                min_idx = j
        number_list[i], number_list[min_idx] = number_list[min_idx], number_list[i]

    # unique 값 정리
    unique = []
    for i in range(N):
        if number_list[i] not in unique:
            unique.append(number_list[i])
    
    print(f'#{tc} {unique[K - 1]}')
    
    
    

# count로 해보기
T = int(input())

for tc in range(1, T + 1):
    N, K = map(int, input().split())
    
    number_list = list(map(int, input().split()))