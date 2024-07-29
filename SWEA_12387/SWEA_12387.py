T = int(input())

for tc in range(1, T + 1):
    n, m = map(int, input().split())
    num_list = list(map(int, input().split()))

    sum_list = [0] * n
    sum_list[0] = num_list[0]

    for i in range(1, n):
        sum_list[i] = sum_list[i - 1] + num_list[i]

    min_sum = sum_list[m - 1]
    max_sum = sum_list[m - 1]

    for j in range(m, n):
        section_sum = sum_list[j] - sum_list[j - m]
        if section_sum < min_sum:
            min_sum = section_sum
        elif section_sum > max_sum:
            max_sum = section_sum

    print(f'#{tc} {max_sum - min_sum}')



