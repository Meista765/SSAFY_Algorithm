import sys
sys.stdin = open("C:/Users/82108/Downloads/input.txt", "r")
#input = sys.stdin.readline

# 반복문 사용 (시간 초과)
arr_size = int(input())  # 배열 크기
arr = list(map(int, input().split()))  # 배열

for i in range(arr_size):
    if i+1 != arr_size:
        for j in range(i+1, arr_size):
            if arr[i] < arr[j]:
                print(arr[j], end=' ')
                break
        else:
            print(-1, end=' ')
    else:
        print(-1, end=' ')