import sys
sys.stdin = open('input.txt')

def back_track(n):
    global max_val

    if n == count:
        max_val = max(max_val,int(''.join(map(str,num_lst))))
        return


    else:

        for i in range(length):
            for j in range(i+1,length):
                num_lst[i], num_lst[j] = num_lst[j], num_lst[i]

                # 가지치기
                # 이전에 같은 레벨에서 같은 숫자인 경우가 있으면 중복되는 것이기 때문에
                # 이전에 없던 내용일 때만 재귀 실행
                cur_price = int(''.join(map(str, num_lst)))
                if (n,cur_price) not in v:
                    back_track(n + 1)
                    v.append((n, cur_price))
                num_lst[i], num_lst[j] = num_lst[j], num_lst[i]



T = int(input())
for test_case in range(1,T+1):
    num, count = input().split()        # num: 숫자판, count: 교환횟수
    count = int(count)                  # 교환횟수 정수화
    num_lst = list(map(int,list(num)))
    length = len(num_lst)               # 숫자카드 갯수
    answer = 0
    v = []                              # 같은 레벨에서 같은 숫자면 가지치기 하기 위해 리스트를 만들어 저장
    max_val = 0
    back_track(0)
    print(f'#{test_case} {max_val}')