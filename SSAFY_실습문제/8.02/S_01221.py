import sys
sys.stdin = open('input.txt','r')

T = int(input())

for test_case in range(1,T+1):

    tc, N = input().split()
    N = int(N)
    lst = list(input().split()) # 정렬시킬 배열
    arr = []

    cnt_dic = {'ZRO':0,
               'ONE':0,
               'TWO':0,
               'THR':0,
               'FOR':0,
               'FIV':0,
               'SIX':0,
               'SVN':0,
               'EGT':0,
               'NIN':0
               }


    for i in range(N):             # cnt_dic 만들기
        cnt_dic[lst[i]] += 1

    for k,v in cnt_dic.items():
        arr += [k] * v
    print(f'{tc}')
    print(*arr)











