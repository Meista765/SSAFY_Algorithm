def solution(sequence, k):  # k: 목표 부분 수열 합
    answer = []
    
    start = 0  # start 포인터
    end = 0  # end 포인터
    
    arr_sum = sequence[0]  # 부분 수열 합 초기화
    diff = 1000000  # sequence의 최대 길이보다 긴 수
    
    while True:
        try:
            if arr_sum < k:  # 부분 수열 합이 k보다 작으면
                end += 1  # end 포인터를 하나 올리고
                arr_sum += sequence[end]  # 부분 수열 합에 증가한 end 포인터 위치에 해당하는 값 더하기
            elif arr_sum > k:  # 부분 수열 합이 k보다 크면
                arr_sum -= sequence[start]  # 부분 수열 합에서 현재 start 포인터 위치에 해당하는 값 빼기
                start += 1  # start 포인터 하나 올리기
            else:  # 부분 수열 합이 k와 같으면
                if diff > end - start:  # 현 인덱스 범위를 계산하고, 이전 diff보다 작으면
                    diff = end - start  # diff를 현 인덱스 범위로 갱신
                    answer = [start, end]  # answer를 현재 투 포인터 인덱스 값으로 갱신
                end += 1
                arr_sum += sequence[end]
                arr_sum -= sequence[start]
                start += 1
        except IndexError:  # end가 인덱스 한계를 넘어가서 인덱스 에러가 나면
            break  # 반복문 종료
        
    return answer


print(solution([1, 2, 3, 4, 5], 7))
print(solution([1, 1, 1, 2, 3, 4, 5], 5))
print(solution([2, 2, 2, 2, 2], 6))