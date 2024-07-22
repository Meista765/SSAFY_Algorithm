import sys
input = sys.stdin.readline

N, T= map(int,input().split())

num_list = list(map(int,input().split()))

# 구간 합 구하기
section_sum_list = [0]
num = 0
for number in num_list:
    num += number
    section_sum_list.append(num)


for test_case in range(1,T+1):
    i,j = map(int,input().split())
    answer = section_sum_list[j] - section_sum_list[i-1] 
    print(answer)