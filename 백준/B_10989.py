import sys
input = sys.stdin.readline

N = int(input())


count_list = [0] * 10001

# count_list만들기
for i in range(N):
    count_list[int(input())] += 1

for i in range(10001):
    if count_list[i] !=0:
        for _ in range(count_list[i]):
            print(i)

