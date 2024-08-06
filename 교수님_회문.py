N = 8
arr = 'ACAACABC'
M = 4       # 찾을 회문의 길이

for s in range(0, N-M + 1):
    e = s + M - 1
    for i in range(M//2):
        # arr[s + i] <-> arr[e - i]
        if arr[s + i] != arr[e - i]:
            print(s, '회문이 아님.')
            break
    else:
        print(s, '회문입니다.')