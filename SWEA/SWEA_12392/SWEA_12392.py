import sys
sys.stdin = open("C:/Users/SSAFY/Desktop/스터디/SSAFY_Algorithm/SWEA/SWEA_12392/sample_input.txt", "r")
# input = sys.stdin.readline

def counting_sort(arr):
    n = len(arr)
    
    max_value = arr[0]
    for i in range(1, len(arr)):
        if arr[i] > max_value:
            max_value = arr[i]

    counts = [0] * (max_value + 1)
    for ele in arr:
        counts[ele] += 1

    adj_counts = [0] * (max_value + 1)
    adj_counts[0] = counts[0]

    for i in range(1, max_value + 1):
        adj_counts[i] = adj_counts[i - 1] + counts[i]

    sorted_list = [0] * n
    for j in range(n - 1, -1, -1):  
        element = arr[j]
        adj_counts[element] -= 1
        sort_idx = adj_counts[element]
        sorted_list[sort_idx] = element

    return sorted_list

T = int(input())

for tc in range(1, T + 1):
    n = int(input())
    number_list = list(map(int, input().split()))
    sorted_list = counting_sort(number_list)
    ans = []

    min_idx = 0
    max_idx = n - 1
    while min_idx <= 4:
        ans.append(sorted_list[max_idx])
        ans.append(sorted_list[min_idx])

        max_idx -= 1
        min_idx += 1
    
    print(f'#{tc}', *ans)




