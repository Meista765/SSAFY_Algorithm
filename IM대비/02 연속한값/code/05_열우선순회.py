# 열 우선 순회
print('열 우선 순회')
arr = [[0] * 7 for _ in range(7)]

num = 1
for i in range(7):
    for j in range(7):
        arr[j][i] = num
        num += 1

for arr_i in arr:
    print(*arr_i)


print('행 우선 순회')
arr = [[0] * 7 for _ in range(7)]

num = 1
for i in range(7):
    for j in range(7):
        arr[i][j] = num
        num += 1

for arr_i in arr:
    print(*arr_i)