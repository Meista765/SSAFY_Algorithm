N = int(input())    # 수의 개수

lst =[int(input()) for _ in range(N)] # 리스트에 저장

for i in range(N-1):
    for j in range(N-1-i):
        if lst[j] > lst[j+1]:
            lst[j], lst[j+1] = lst[j+1], lst[j]
for i in range(N):
    print(lst[i])
    