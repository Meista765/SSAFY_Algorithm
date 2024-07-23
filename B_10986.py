N, M = map(int,input().split())

num_lst = list(map(int, input().split()))

# 합 배열 구하기

number = 0
sum_lst = [0] # 합 배열
c = [0] * M


for i in range(1,N):
    number += num_lst[i]
    sum_lst.append(number)



# 합 나머지 배열 구하기

for j in range(N):




