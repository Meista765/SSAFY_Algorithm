import sys
sys.stdin = open('input.txt')

'''
왼쪽으로 가는 것을 -1으로
오른쪽으로 가는 것을 1로
한번에 찾으면 0 '''
def binary_search(l,r,key,check):

    while l <= r:
        mid = (l+r)//2
        if A[mid] == key:
            return True
        elif A[mid] > key:  # 왼쪽 선택
            if check[-1] == 'l':
                return False
            check += 'l'
            r = mid - 1
        else:
            if check[-1] == 'r':
                return False
            check += 'r'
            l = mid + 1

    return False


T = int(input())
for test_case in range(1,T+1):
    N, M = map(int,input().split())
    A = sorted(list(map(int,input().split())))
    B = list(map(int,input().split()))
    cnt = 0
    flag = True
    for i in range(M):
        key = B[i]
        if binary_search(0, N-1, key, ' '):
            cnt += 1
    print(f'#{test_case} {cnt}')

