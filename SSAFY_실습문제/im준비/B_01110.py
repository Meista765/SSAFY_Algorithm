N = input()
cnt = 0
M = N
while True:
    # 10보다 작으면 2자리 수로 만들기
    if int(M) < 10:
        M = '0'+M
    a = str(int(M[0]) + int(M[-1]))      # 각 자릿 수 더하기
    M = M[-1] + a[-1]                   # 주어진 수의 오른쪽 자리의 수와 각 자릿 수를 더한 것의 오른쪽 자리 수를 이어 붙인다.
    cnt += 1
    if int(N) == int(M):                          # 원상복구 되면 멈추기
        break

print(cnt)