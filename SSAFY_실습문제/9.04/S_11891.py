import sys
sys.stdin = open('input.txt')

def merge_sort(lst):

    # 1이 될 때까지
    if len(lst) == 1:
        return lst

    # 분할
    mid = len(lst) // 2
    left = merge_sort(lst[:mid])
    right = merge_sort(lst[mid:])

    return merge(left, right)

def merge(left,right):
    global cnt
    l = r = 0
    result = [0] * (len(left) + len(right))

    if left[-1] > right[-1]:
        cnt +=1

    while l < len(left) and r < len(right):
        if left[l] < right[r]:
            result[l + r] = left[l]
            l += 1
        else:
            result[l + r] = right[r]
            r += 1

    while l < len(left):
        result[l + r] = left[l]
        l += 1
    while r < len(right):
        result[l + r] = right[r]
        r += 1

    return result




T = int(input())
for test_case in range(1,T+1):
    N = int(input())
    arr = list(map(int,input().split()))
    cnt = 0
    result = merge_sort(arr)

    print(f'#{test_case} {result[N//2]} {cnt}')
