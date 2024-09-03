'''
연속인 숫자가 3개 -> run
같은 숫자가 3개 -> triplet
'''

import sys
sys.stdin = open('input.txt')

def run_check(lst):
    idx = 0
    while idx < 8: # 0~7
        if lst[idx] >= 1 and lst[idx+1] >= 1 and lst[idx+2] >= 1:
            return True
        idx += 1
    return False

def triplet_check(lst):
    idx = 0
    while idx < 10:
        if lst[idx] >= 3:
            return True
        idx += 1
    return False

T = int(input())
for test_case in range(1,T+1):
    card = list(map(int,input().split()))
    p1 = [0] * 10          # player1
    p2 = [0] * 10          # player2


    for i in range(12):
        if i % 2 == 0:       # player1이 받을 차례
            p1[card[i]] += 1
            if i >= 4:
                if run_check(p1) or triplet_check(p1):
                    print(f'#{test_case} {1}')
                    break

        else:
            p2[card[i]] += 1
            if i >= 4:
                if run_check(p2) or triplet_check(p2):
                    print(f'#{test_case} {2}')
                    break
    else:
        print(f'#{test_case} {0}')


