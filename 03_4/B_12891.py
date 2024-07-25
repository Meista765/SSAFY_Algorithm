import sys
sys.stdin = open("C:/Users/SSAFY/Downloads/sample_input.txt", "r")
#input = sys.stdin.readline

dna_len, pw_len = map(int, input().split())  # dna 문자열 길이, 비밀번호 길이 입력
dna_seq = list(input())  # dna 서열 입력
check_list = list(map(int, input().split()))  # 비밀번호에 포함되어야 하는 각 염기의 최소 갯수 리스트 (ACGT순)
possible_pw_count = 0  # 가능한 비밀번호 수

start = 0  # 왼쪽 포인터
end = pw_len  # 오른쪽 포인터

window = dna_seq[start:end]  # 첫번째 범위
current_list = [window.count('A'), window.count('C'), window.count('G'), window.count('T')]

def add_base(current_list, base):
    if base == 'A':
        current_list[0] += 1
    elif base == 'C':
        current_list[1] += 1
    elif base == 'G':
        current_list[2] += 1
    elif base == 'T':
        current_list[3] += 1
    return current_list

def remove_base(current_list, base):
    if base == 'A':
        current_list[0] -= 1
    elif base == 'C':
        current_list[1] -= 1
    elif base == 'G':
        current_list[2] -= 1
    elif base == 'T':
        current_list[3] -= 1
    return current_list


while True:  # 엔드 포인터가 dna 길이 끝을 넘어가면 반복 종료

    for i in range(4):  # 각 염기별 개수 탐색
        if current_list[i] < check_list[i]:  # 현재 염기 개수가 최소 개수보다 작으면
            break  # 반복 종료
    else:  # 최소 개수 조건 만족하면
        possible_pw_count += 1

    if end > dna_len-1:  # end 포인터가 dna 서열의 마지막 인덱스를 넘어가면
        break  # while문 종료

    current_list = add_base(current_list, dna_seq[end])  # 현재 end 포인터 + 1 위치 염기 수 하나 더하기
    current_list = remove_base(current_list, dna_seq[start])  # 현재 start 포인터 위치 염기 수 하나 빼기
    
    start += 1
    end += 1

print(possible_pw_count)