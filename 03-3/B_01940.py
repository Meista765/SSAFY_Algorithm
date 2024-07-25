import sys
sys.stdin = open("C:/Users/SSAFY/Downloads/sample_input.txt", "r")
#input = sys.stdin.readline

N = int(input())  # 재료의 개수
goal_of_sum = int(input())  # 갑옷이 완성되기 위한 재료 고유번호의 합
ingr_num = list(map(int, input().split()))  # 재료들의 고유번호 리스트

ingr_num.sort()  # 오름차순 정렬

front = 0  # 앞쪽 포인터
end = len(ingr_num) - 1  # 뒷쪽 포인터
count = 0  # 갑옷을 만들 수 있는 경우의 수

while front < end:  # 왼쪽 포인터가 오른쪽 포인터보다 더 커지거나 두 포인터 위치가 같아지면 반복 종료
    two_pointer_sum = ingr_num[front] + ingr_num[end]  # 두 고유번호의 합

    if two_pointer_sum < goal_of_sum:  # 두 고유번호의 합이 목표 합보다 작으면 
        front += 1  # 왼쪽 포인터 1 증가
    elif two_pointer_sum > goal_of_sum:  # 두 고유번호의 합이 목표 합보다 크면
        end -= 1  # 오른쪽 포인터 1 감소
    else:  # 두 고유번호의 합이 목표 합과 같으면
        count += 1  # 경우의 수 1개 증가
        front += 1  # 왼쪽 포인터 1 증가
        end -= 1  # 오른쪽 포인터 1 감소

print(count)