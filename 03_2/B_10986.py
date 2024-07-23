import sys
sys.stdin = open("C:/Users/SSAFY/Downloads/sample_input.txt", "r")

# import sys
# input = sys.stdin.readline

N, M = map(int, input().split())  # N: 숫자 개수, M: 나누는 수
num_list = list(map(int, input().split()))  # 주어지는 숫자 리스트
remainder_counts = [0] * M  # 나머지 종류별 개수 리스트
prefix_list = []  # 누적 합을 저장할 리스트
answer = 0  # 전체 경우의 수

temp_sum = 0  # 반복 마다 누적합 값을 저장할 변수
for num in num_list:  # 주어진 숫자들 순회
    temp_sum += num  # 숫자를 temp_sum에 더하기
    prefix_list.append(temp_sum)  # temp_sum에 저장된 누적합 값을 prefix_list에 저장

for prefix in prefix_list:  # 누적 합 저장된 리스트 순회
    remainder = prefix % M  # 각 누적 합에 M을 나눈 나머지
    if remainder == 0:  # 나머지가 0이면
        answer += 1  # 전체 경우의 수에 1 더하기
    remainder_counts[remainder] += 1  # 나머지 리스트에서 나머지에 해당하는 인덱스의 값을 1 올림

for cnt in remainder_counts:  # 나머지 종류별 개수 순회
    if cnt > 1:  # 개수가 1보다 크면
        answer += (cnt*(cnt-1)) // 2  # (cnt C 2) 조합 계산

print(answer)  # 전체 경우의 수 출력