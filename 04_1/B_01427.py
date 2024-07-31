lst = list(map(int, input())) # 리스트로 저장

for i in range(len(lst)):
    for j in range(i+1, len(lst)):
        if lst[i] < lst[j]:
            lst[i], lst[j] = lst[j], lst[i]

for i in range(len(lst)):
    print(lst[i], end='')