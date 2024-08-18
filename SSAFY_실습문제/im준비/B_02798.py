# def comb(k,s):
#     global min_diff
#     result = 0
#     if k == R:
#         if abs(M-sum(pick)) < min_diff:
#             min_diff = abs(M-sum(pick))
#             result = sum(pick)
#     else:
#         remain = R - (k+1)
#         for i in range(s,N-remain):
#             pick[k] = arr[i]
#             comb(k+1,i+1)
#
#     return result

N, M = map(int,input().split())     # N: 카드의 개수 M: 블랙잭 숫자
arr = list(map(int,input().split()))


min_diff = float('inf')
for i in range(N-2):
    for j in range(i+1,N-1):
        for k in range(j+1,N):
            black_sum = arr[i]+arr[j]+arr[k]
            if M >= black_sum:
                if min_diff > M - black_sum:
                    min_diff = M-black_sum
                    ans = black_sum
print(ans)

