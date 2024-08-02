# 버블 정렬 프로그램 1
# 이해 안됨 ㅠㅠ
import sys
sys.stdin = open("C:/Users/SSAFY/Downloads/sample_input.txt", "r")
#input = sys.stdin.readline

N = int(input())  # 입력 받는 수의 개수
arr = [(int(input()), i) for i in range(N)]  # (값, 인덱스) 형태로 리스트에 저장

max_v = 0
sorted_arr = sorted(arr, key=lambda x: x[0])

for i in range(N):
    if max_v < sorted_arr[i][1] - i:  # 정렬 전 index - 정렬 후 index 계산의 최댓값 저장
        max_v = sorted_arr[i][1] - i

print(max_v + 1)  # swap이 일어나지 않는 반복문이 한 번 더 실행되는 것을 감안해 최댓값에 1 더하기ㅣㄴ
