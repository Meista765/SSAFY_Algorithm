import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

T = int(input())  # 테스트케이스의 개수
for tc in range(1, T+1):
    N, M = map(int, input().split())  # N: 정수의 개수, M: 구간의 개수
    num_list = list(map(int, input().split()))  # 숫자 리스트

    count = 0
    min_prefix_sum = float('inf')  # 초기값 무한대로 설정
    max_prefix_sum = float('-inf')  # 초기값 무한소로 설정
    while True:
        try:
            prefix_sum = 0  # 현재 범위의 구간합
            # 범위 M만큼 구간 합 구하기
            for i in range(M):
                prefix_sum += num_list[count+i]
            # 최소 구간합보다 현 구간합이 더 작으면 최소 구간합 갱신
            if prefix_sum < min_prefix_sum:
                min_prefix_sum = prefix_sum
            # 최대 구간합보다 현 구간합이 더 크면 최대 구간합 갱신
            if prefix_sum > max_prefix_sum:
                max_prefix_sum = prefix_sum
            count += 1  # count 1 증가
        except IndexError:  # 인덱스가 숫자 리스트 범위를 벗어나면 
            break  # 반복문 종료

    print(f'#{tc} {max_prefix_sum - min_prefix_sum}')  # 테스트케이스 별 최대값에서 최소값을 뺀 값 출력