import sys
sys.stdin = open('input.txt')

def back_track(n):  #



T = int(input())
for test_case in range(1,T+1):
    num, count = input().split()    # num: 숫자판, count: 교환횟수
    count = int(count)
    num_lst = list(map(int,list(num)))
    n = len(num_lst)
    answer = 0