N = int(input())
arr = list(map(int,input().split()))

max_length = 0
start = 0 # 시작 인덱스
end = 0   # 종료 인덱스

for i in range(N-1):

    if arr[i] < arr[i+1]:
        end = i+1

    else: 
        length = arr[end] - arr[start]
        
        if max_length < length:
            max_length = length

        
        start = i+1
        end = i+1

if arr[start] < arr[end]:

    length = arr[end]-arr[start]
    if max_length < length:
        max_length = length



print(max_length)