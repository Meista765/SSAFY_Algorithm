import sys
#sys.stdin = open("C:/Users/82108/Downloads/input.txt", "r")
input = sys.stdin.readline

N = int(input())  # 자연수 입력
count = 1  # 가지수 (N 하나만 있을 때 경우의 수 1개 기본 추가)
start_idx = 1  # start point
end_idx = 1  # end point
sum = 1  # 총합 (1부터 시작하기 때문에 기본 1부터 시작)

while end_idx != N:  # end point가 N에 도달할 때까지 반복
    if sum < N:  # sum이 N보다 작으면
        end_idx += 1  # end point 증가
        sum += end_idx  # sum에 증가된 end point 더하기
    elif sum > N:  # sum이 N보다 크면
        sum -= start_idx  # 기존 start point 값을 sum에서 빼기
        start_idx += 1  # start point 증가
    else:  # # sum과 N이 같으면
        count += 1  # count 하나 올리기
        end_idx += 1  # end point 증가
        sum += end_idx  # sum에 증가된 end point 더하기

print(count)  # 총 가지수 출력