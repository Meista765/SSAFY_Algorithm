A, B = map(int,input().split())

C = [0] * 1001
j = 1
k = 1
flag = False
for i in range(1,B+1):
    for j in range(0,i):
        C[k] = i
        k += 1
        if k > 1000:
            flag = True
            break
    if flag:
        break


ans = 0

for i in range(A,B+1):
    ans += C[i]

print(ans)