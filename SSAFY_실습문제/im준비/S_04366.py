def bank(two,three):

    N = len(two)  # 2진수 자릿수
    M = len(three)  # 3진수 자릿수

    for i in range(N):
        two_list = list(two)
        if two_list[i] == '1':
            two_list[i] = '0'
            original_two = ''.join(two_list)
        else:
            two_list[i] = '1'
            original_two = ''.join(two_list)

        for j in range(M):
            three_list = list(three)
            if three_list[j] == '0':
                for k in ['1', '2']:
                    three_list[j] = k
                    original_three = ''.join(three_list)
                    if int(original_two,2) == int(original_three,3):
                        return int(original_two,2)
            elif three_list[j] == '1':
                for k in ['0', '2']:
                    three_list[j] = k
                    original_three = ''.join(three_list)
                    if int(original_two, 2) == int(original_three, 3):
                        return int(original_two, 2)
            else:
                for k in ['0', '1']:
                    three_list[j] = k
                    original_three = ''.join(three_list)
                    if int(original_two, 2) == int(original_three, 3):
                        return int(original_two, 2)

T = int(input())

for test_case in range(1,T+1):
    two = input() # 2진수
    three = input() # 3진수

    result = bank(two,three)
    print(f'#{test_case} {result}')