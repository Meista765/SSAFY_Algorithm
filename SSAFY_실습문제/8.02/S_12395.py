T = int(input())

for test_case in range(1,T+1):
    str1 = input()
    str2 = input()
    max_cnt = 0
    for i in range(len(str1)):

        cnt = 0
        for j in range(len(str2)):
            if str1[i] == str2[j]:
                cnt += 1
        if max_cnt < cnt:
            max_cnt = cnt

    print(f'#{test_case} {max_cnt}')




