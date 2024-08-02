import sys
input = sys.stdin.readline

n = int(input())
number_list = list(map(int, input().split()))

number_list.sort()


cnt = 0

for i in range(n):
    find = number_list[i]
    start_index = 0
    end_index = n-1
    while start_index < end_index:
        
        if number_list[start_index]+number_list[end_index] == find:
            if start_index != i and end_index != i:
                cnt += 1
                break
            elif start_index == i:
                start_index += 1
            elif end_index == i:
                end_index -= 1
        
        elif number_list[start_index] + number_list[end_index] > find:
            end_index -= 1
        
        else:
            start_index += 1

print(cnt)