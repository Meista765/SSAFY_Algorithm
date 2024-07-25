# N = int(input())

# count = 1
# start_idx = 1
# end_idx = 1
# sum = 1

# while end_idx != N:
#     if sum == N:
#         count += 1
#         end_idx += 1
#         sum += end_idx
#     elif sum > N:
#         sum -= start_idx
#         start_idx += 1
#     else:
#         end_idx += 1
#         sum += end_idx

# print(count)

N = int(input())

sum = 1
cnt = 1
start_idx = 1
end_idx = 1

while end_idx != N:
    if sum > N:
        sum -= start_idx
        start_idx += 1
    elif sum < N:
        end_idx += 1
        sum += end_idx
    else:
        cnt += 1
        end_idx += 1
        sum += end_idx
print(cnt)


