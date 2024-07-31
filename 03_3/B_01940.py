# 투 포인터 이동 원칙, 정렬 !!!
# A[i] + A[j] > M: j--;
# A[i] + A[j] < M: i++;
# A[i] + A[j] == M: i++; j--; count++;

import sys
#input = sys.stdin.readline
sys.stdin = open("C:/Users/SSAFY/Desktop/input.txt", "r")

N = int(input())
M = int(input())
num_lst = list(map(int,input().split()))
num_lst.sort()
i = 0
j = N-1
count = 0

# print(num_lst)
while i < j:
    if num_lst[i] + num_lst[j] < M:
        i += 1
    elif num_lst[i] + num_lst[j] > M:
        j -= 1
    else:
        count += 1
        i += 1
        j -= 1
print(count)

