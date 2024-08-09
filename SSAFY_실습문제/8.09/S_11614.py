# 가위: 1, 바위: 2, 보: 3

import sys
sys.stdin = open('input.txt')

def divide_conquer(s,e):

    if s == e:
        return s
    else:
        mid = (s+e)//2
        # 재귀
        left_idx = divide_conquer(s,mid)
        right_idx = divide_conquer(mid+1,e)

        if arr[left_idx] == 1:         # 가위
            if arr[right_idx] == 1:
                return left_idx
            elif arr[right_idx] == 2:
                return right_idx
            elif arr[right_idx] == 3:
                return left_idx

        elif arr[left_idx] == 2:        # 바위
            if arr[right_idx] == 1:
                return left_idx
            elif arr[right_idx] == 2:
                return left_idx
            elif arr[right_idx] == 3:
                return right_idx

        elif arr[left_idx] == 3:        # 보
            if arr[right_idx] == 1:
                return right_idx
            elif arr[right_idx] == 2:
                return left_idx
            elif arr[right_idx] == 3:
                return left_idx


T = int(input())
for test_case in range(1,T+1):
    N = int(input())        # 학생 수
    arr = list(map(int,input().split()))  # 학생들이 가지고 있는 카드드
    print(f'#{test_case} {divide_conquer(0, N - 1) + 1}')
