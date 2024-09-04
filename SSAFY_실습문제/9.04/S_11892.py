import sys
sys.stdin = open('input.txt')

def quick_sort(left,right):
    if left >= right:
        return

    pivot = arr[left]
    i = left
    j = right
    while i <= j:
        while i <= right and pivot >= arr[i]:
            i += 1
        while pivot < arr[j]:
            j -= 1
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]

    arr[left], arr[j] = arr[j], arr[left]
    quick_sort(left,j-1)
    quick_sort(j+1,right)


T = int(input())
for test_case in range(1,T+1):
    N = int(input())
    arr = list(map(int,input().split()))
    quick_sort(0,N-1)
    print(f'#{test_case} {arr[N//2]}')