T = int(input())

for test_case in range(1,T+1):
    num_str = float(input())

    ans = ''

    while num_str != 0:
        num_str = num_str * 2
        tmp = str(num_str)[0]
        ans += tmp
        num_str -= int(tmp)


    if len(ans) >= 13:
        print(f'#{test_case} overflow')
    else:
        print(f'#{test_case} {ans}')