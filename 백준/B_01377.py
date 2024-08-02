N = int(input())
A = []

for i in range(N):
    A.append((int(input()),i))

max_count = 0

sorted_A = sorted(A)

for i in range(N):
    if max_count < sorted_A[i][1] - i:
        max_count = sorted_A[i][1] - i
print(max_count+1)