# 수 찾기
import sys
#input = sys.stdin.readline
sys.stdin = open("C:/Users/82108/Downloads/sample_input.txt", "r")

def binary_search(A_len, B_len, A, B):
    A.sort()        # 일단 A 정렬
    
    for b in B:     # B 원소 순회
        start = 0
        end = A_len - 1
        find_flag = False
        while start <= end:
            mid = (start + end) // 2
            if A[mid] > b:      # b가 중간값보다 작으면
                end = mid - 1
            elif A[mid] < b:    # b가 중간값보다 크면
                start = mid + 1
            else:               # b가 중간값이면
                print(1)
                find_flag = True
                break
        if not find_flag:
            print(0)                

A_len = int(input())    # N: A 데이터 개수
A = list(map(int, input().split()))   # A: 배열 A
B_len = int(input())    # M: B 데이터 개수
B = list(map(int, input().split()))   # B: 배열 B

binary_search(A_len, B_len, A, B)