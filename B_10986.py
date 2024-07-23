N, M = map(int,input().split())

num_lst = list(map(int, input().split()))

# 합 배열 구하기

number = 0
S = [0] * N # 합 배열
C = [0] * M # 나머지 배열

S[0] = num_lst[0]

# 합 배열 만들기

for i in range(1,N):
    S[i] = S[i-1] + num_lst[i]

# 합 나머지 배열 구하기

cnt = 0  # 합 나머지 배열이 0인 것 카운트
for j in range(N):
    remain_num = S[j] % M
    if remain_num == 0:
        cnt += 1
    C[remain_num] += 1


for k in range(M):
    if C[k] > 1:
        
        cnt  += (C[k] * (C[k]-1)) //2


print(cnt)




