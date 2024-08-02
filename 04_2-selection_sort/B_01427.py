num_list = list(map(int, list(input())))
num_list_size = len(num_list)
for i in range(num_list_size-1):
    max_idx = i
    for j in range(i, num_list_size):
        if num_list[max_idx] < num_list[j]:
            max_idx = j
    num_list[i], num_list[max_idx] = num_list[max_idx], num_list[i]

for num in num_list:
    print(str(num), end='')