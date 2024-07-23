# 합 배열 만드는 공식
# S[i] = S[i-1] + A[i]

# 구간 합 구하는 공식
# S[j] - S[i-1]


'''N, M = map(int, input().split())
lst = list(map(int, input().split()))

S = list()
S.append(lst[0])
for idx in range(1, len(lst)):
    S.append(S[idx-1]+lst[idx])
# print(S)

for _ in range(M):
    i, j = map(int, input().split())
    if i == 1:
        print(S[j-1])
    else:
        print(S[j-1]-S[i-2])'''


# 교재
import sys
input = sys.stdin.readline
N, M = map(int, input().split())
lst = list(map(int, input().split()))
S = [0] # 리스트 인지 부조화 막기 위해서 0 넣기
temp = 0

for i in lst:
    temp = temp + i
    S.append(temp)

for i in range(M):
    i, j = map(int, input().split())
    print(S[j] - S[i-1])

