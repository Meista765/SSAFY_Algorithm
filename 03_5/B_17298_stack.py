import sys
sys.stdin = open("C:/Users/82108/Downloads/input.txt", "r")
#input = sys.stdin.readline

# 반복문 사용 (시간 초과)
# arr_size = int(input())  # 배열 크기
# arr = list(map(int, input().split()))  # 배열

# for i in range(arr_size):
#     if i+1 != arr_size:
#         for j in range(i+1, arr_size):
#             if arr[i] < arr[j]:
#                 print(arr[j], end=' ')
#                 break
#         else:
#             print(-1, end=' ')
#     else:
#         print(-1, end=' ')

# 스택 사용
arr_size = int(input())  # 배열 크기
arr = list(map(int, input().split()))  # 배열
answer = [0] * arr_size
stack = []  # 인덱스 값을 넣기

for i in range(arr_size):
    # 스택이 비지 않고, 현재 수열값이 top에 해당하는 수열보다 클 때까지 반복
    while stack and arr[i] > arr[stack[-1]]:
        answer[stack.pop()] = arr[i]  # 정답 리스트에 오큰수를 현재 수열로 저장
    stack.append(i)
    
while stack:  # 반복문을 다 돌고 나왔는데 스택이 비어 있지 않다면 빌 때까지
    answer[stack.pop()] = -1
    
result = ''

for x in answer:
    result += str(x) + ' '

print(result)