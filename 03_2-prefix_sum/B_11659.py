import sys
sys.stdin = open("C:/Users/82108/Downloads/input.txt", "r")

import sys
input = sys.stdin.readline

N, M = map(int, input().split())  # N: 수의 개수, M: 합을 구해야 하는 횟수
num_list = list(map(int, input().split()))  # N개의 수

# 누적 합 구하기
sum_list = [0]  # 누적 합 리스트 초기화
temp_sum = 0  # 구간 합
for num in num_list:  # num_list 내 숫자 loop
    temp_sum += num  # temp_sum에 숫자를 하나씩 더하고
    sum_list.append(temp_sum)  # 각 구간 합을 sum_list에 저장

for _ in range(M):  # M번 loop
    i, j = map(int, input().split())  # 질의 범위 받기
    print(sum_list[j] - sum_list[i-1])  # 구간 합 출력