import sys
sys.stdin = open('C:/Users/SSAFY/Desktop/git/SSAFY_Algorithm/SWEA/SWEA_01240_단순이진암호코드/input.txt', 'r')

code_dict = {
    '0001101':'0',
    '0011001':'1',
    '0010011':'2',
    '0111101':'3',
    '0100011':'4',
    '0110001':'5',
    '0101111':'6',
    '0111011':'7',
    '0110111':'8',
    '0001011':'9'
}

T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    matrix = [list(input()) for _ in range(N)]
    code_list = []
    
    # 일단 1이 있는 행 찾기
    for r in range(N):
        if '1' in matrix[r]:
            break
            
    # 암호 찾는 배열
    code_inc = matrix[r]
    
    # 암호가 끝나는 컬럼 인덱스 찾기
    for c in range(M - 1, -1, -1):
        if code_inc[c] == '1':
            break
    
    # 암호가 속한 배열만 뽑아보자
    code_inc = code_inc[(c - 55):(c + 1)]
    
    # 암호 넣자
    code_digit = ''
    for start_idx in range(0, len(code_inc), 7):
        for digit in code_inc[start_idx:(start_idx + 7)]:
            code_digit += digit
        if code_digit in code_dict:
            # 이거 잘못 합쳐짐 이거 고치면 거의 끝난다
            code_list.append(int(code_dict[code_digit]))
    
    print(code_list)
    