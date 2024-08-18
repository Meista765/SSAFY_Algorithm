N = int(input())    # 스위치 개수
arr = [0] + list(map(int,input().split()))    # 스위치 상태
M = int(input())    # 학생 수
gender = [0] * M
number = [0] * M

for i in range(M):
    gender[i], number[i] = map(int,input().split())


for i in range(M):
    if gender[i] == 1:  # 남자이면
        n = 1
        while number[i] * n <= N:
            if arr[number[i]*n] == 1:
                arr[number[i] * n] = 0
            else:
                arr[number[i] * n] = 1
            n += 1
    else:               # 여자이면
        s = number[i] - 1
        e = number[i] + 1
        while s >= 1 and e <= N:
            if arr[s] == arr[e]:    # 대칭이면
                s -= 1
                e += 1
            else:
                break
        for j in range(s+1,e):
            if arr[j] == 1:
                arr[j] = 0
            else:
                arr[j] = 1

for i in range(1,N+1):
    print(arr[i], end = ' ')
    if i % 20 == 0:
        print()
