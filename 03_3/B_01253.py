import sys
sys.stdin = open("C:/Users/SSAFY/Downloads/sample_input.txt", "r")
#input = sys.stdin.readline

N = int(input())  # 수의 개수
num_list = list(map(int, input().split()))  # 숫자 리스트 (음수도 올 수 있음)
good_count = 0  # 좋은 수의 개수

num_list.sort()  # 숫자 리스트 오름차순 정렬

for i in range(N):  # 숫자 리스트 내 모든 수 순회
    goal_num = num_list[i]
    start = 0  # 왼쪽 포인터 인덱스
    end = N-1  # 오른쪽 포인터 인덱스
    
    while start < end:  # 왼쪽 포인터가 오른쪽 포인터보다 커지거나 두 포인터의 위치가 같아지면 반복 종료
        two_pointer_sum = num_list[start] + num_list[end]  # 두 수의 합

        if two_pointer_sum == goal_num:  # 두 수의 합이 해당 수와 같으면
            if i != start and i != end:  # 두 포인터가 모두 i가 아니면
                good_count += 1  # 좋은 수의 개수 하나 증가
                break  # 반복 종료
            elif start == i:  # 왼쪽 포인터가 i이면
                start += 1  # 왼쪽 포인터를 오른쪽으로 한칸 이동
            elif end == i:  # 오른쪽 포인터가 i이면
                end -= 1  # 오른쪽 포인터를 왼쪽으로 한칸 이동
        elif two_pointer_sum < goal_num:  # 두 수의 합이 해당 수보다 작으면
            start += 1  # 왼쪽 포인터 오른쪽으로 한칸 이동
        else:  # 두 수의 합이 해당 수보다 크면
            end -= 1  # 오른쪽 포인터 왼쪽으로 한칸 이동

print(good_count)