# 1차 배열의 구간 표현
N = 10
arr = [i for i in range(N)]  # arr[i] = i 를 저장
print(*arr)

# 1. 구간의 시작과 끝
s = 3
e = 7
for i in range(s, e + 1):
    arr[i] = '-'
print(*arr)
# ==================================
# 2. 구간의 시작과 길이
N = 10
arr = [i for i in range(N)]  # arr[i] = i 를 저장
s = 3
l = 5
for i in range(s, s + l): # s부터 s + l - 1
    arr[i] = '+'
print(*arr)

# ==================================
# 3. 모든 구간 탐색
M = 3
arr = [i for i in range(N)]

for i in range(N - M + 1):
    print(f'현재 시작 인덱스: {i}')
    for j in range(M):
        print(arr[i + j], end = ' ')
    print()

# ==================================
# 4. 문자열 패턴 매칭
text = 'wehqssapasiessapqwehgh'
pattern = 'ssap'
N = len(text)
M = len(pattern)

cnt = 0
for i in range(N - M + 1):
    for j in range(M):
        if text[i + j] != pattern[j]:
            break
    else:
        cnt += 1

print(f'패턴 발견 수: {cnt}')
