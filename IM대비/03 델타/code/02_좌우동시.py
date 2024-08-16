N = 10
arr = [0] * N

s = 4
l = 4
arr[s] = '*'

for i in range(1, l + 1):
    a = s - i
    b = s + i
    if a < 0 or b >= N:
        break
    arr[a] = arr[b] = '-'
# ------------------------
print(*arr)