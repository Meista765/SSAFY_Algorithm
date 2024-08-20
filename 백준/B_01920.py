N = int(input())
arr = list(map(int,input().split()))
arr.sort()
M = int(input())
wanted_number = list(map(int,input().split()))

for i in range(M):
    find = False
    want = wanted_number[i]

    start = 0
    end= N -1
    while start <= end:
        mid = int((start+end)/2)
        mid_val = arr[mid]
        if mid_val > want:
            end = mid - 1
        elif mid_val < want:
            start = mid+1
        else:
            find = True
            break
    if find:
        print(1)
    else:
        print(0)
