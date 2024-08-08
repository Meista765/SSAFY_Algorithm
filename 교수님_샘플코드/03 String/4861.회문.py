import sys; sys.stdin = open('4861.txt', 'r')
N = M = 0
arr = 'asldfleveljlskdf'

# 1. 문자열에서 특정 위치에서 시작하는 길이 M의 회문 체크
# 시작 s, 끝 s + M - 1
s = 0
for i in range(M//2):
    e = s+M-1
    if arr[s+i] != arr[e-i]:   # 대칭하는 두 문자를 비교
        break
else:
    # 회문을 찾음.
    ret = ''
    for j in range(M):
        ret += arr[s + j]

# 2. 모든 시작 위치에서 반복
for s in range(N-M + 1):
    for i in range(M//2):
        e = s+M-1
        if arr[s+i] != arr[e-i]:   # 대칭하는 두 문자를 비교
            break
    else:
        # 회문을 찾음.
        ret = ''
        for j in range(M):
            ret += arr[s + j]

# 3. 모든 행에 대해서 반복
for row in range(N):
    for s in range(N-M + 1):
        for i in range(M//2):
            e = s+M-1
            if arr[row][s+i] != arr[row][e-i]:   # 대칭하는 두 문자를 비교
                break
        else:
            # 회문을 찾음.
            ret = ''
            for j in range(M):
                ret += arr[row][s + j]

# 4. 모든 열에 대해서
for col in range(N):
    for s in range(N-M + 1):
        for i in range(M//2):
            e = s+M-1
            if arr[s+i][col] != arr[e-i][col]:   # 대칭하는 두 문자를 비교
                break
        else:
            # 회문을 찾음.
            ret = ''
            for j in range(M):
                ret += arr[s + j][col]
