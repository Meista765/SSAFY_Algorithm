import sys
sys.stdin = open("C:/Users/82108/Downloads/input.txt", "r")
#input = sys.stdin.readline

arr_size = int(input())  # 배열 크기
arr = list(map(int, input().split()))  # 배열

for i in range(arr_size):
    for j in range(i+1, arr_size):
        