N = input()
scores = input()
sum = 0

lst = scores.split()

M = max(lst)
for idx in lst:
    sum += int(idx)/int(M)*100
print(sum/int(N))  