import sys
input = sys.stdin.readline
N, K= map(int,input().split())
arr =list(map(int,input().split()))

# 퀵 정렬 함수
def quicksort(start,end,k):
    global arr
    if start < end:
        pivot = partition(start,end)
        if pivot ==k:
            return 
        elif k < pivot:
            quicksort(start, pivot-1,k)
        else:
            quicksort(pivot+1,end,k)



# 피벗 구하기 함수
def partition(start,end):
    global arr

    # ???
    if start + 1 == end:
        if arr[start] > arr[end]:
            arr[start],arr[end] = arr[end],arr[start]

        return end
    
    middle = (start+end)//2
    arr[start],arr[middle] = arr[middle],arr[start]
    pivot =  arr[start] # pivot을 시작 위치로
    i = start +1 # 시작위치는 pivot옆으로
    j = end 

    while i <= j:
        while pivot < arr[j] and j >0: # end가 피벗보다 클 때
            j -= 1 # end 위치 왼족으로
        while pivot > arr[i] and i < len(arr) -1:
            i = i+1
        if i<=j:
            arr[i],arr[j] = arr[j], arr[i]
            i += 1
            j -= 1
    arr[start] = arr[j]
    arr[j] = pivot
    return j

quicksort(0,N-1,K-1)
print(arr[K-1])



