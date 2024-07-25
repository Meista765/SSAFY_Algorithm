# 문제 조건 잘 읽기 ... 값이 음수일 수 있다..
# 자기 자신 제외하고 찾아야 함 !

import sys
input = sys.stdin.readline
N =int(input())
A = list(map(int, input().split()))
A.sort
count = 0

for k in range(N):
    find = A[k]
    i = 0
    j = N -1
    while i < j:
        if A[i] + A[j] == find:
            if i != k and j != k:
                count += 1
                break
            elif i == k:
                i += 1
            elif j == k:
                j -= 1
        elif A[i] + A[j] < find:
            i += 1
        else: j -= 1

print(count)

# N = int(input())
# A_i = list(map(int, input().split()))
# count = 0

# for k in range(N):
#      find = A[k]
#      i = 0
#      j = 1
#      while i == j:
#         if A_i[i] + A_i[j] == A[k]:
#             count += 1
#             break
#         elif A_i[i] + A_i[j] < A[k]:
#             j += 1
#         else:
#             i += 1
#         print(count)


    
