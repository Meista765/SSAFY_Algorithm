import sys
sys.stdin = open("C:/Users/82108/Downloads/input.txt", "r")
#input = sys.stdin.readline

T = int(input())  # 테스트 케이스 개수 입력

for tc in range(1, T+1):  # 테스트 케이스 순회
    N, M = map(int, input().split())  # N: 파리 개수 배열 크기, M: 파리채 크기
    prefix_arr = [[0 for _ in range(N+1)] for _ in range(N+1)]  # 누적 합 배열 초기화
    
    # 파리 개수 배열 만들기
    arr = [[0]*(N+1)]  
    for _ in range(N):
        arr.append([0] + list(map(int, input().split())))
        
    # 1행 채우기
    for j in range(1, len(prefix_arr)):
        prefix_arr[1][j] = prefix_arr[1][j-1] + arr[1][j]
        
    # 1열 채우기
    for i in range(1, len(prefix_arr)):
        prefix_arr[i][1] = prefix_arr[i-1][1] + arr[i][1]
    
    # 누적 합 배열 만들기
    for i in range(2, len(prefix_arr)):
        for j in range(2, len(prefix_arr)):
            prefix_arr[i][j] = prefix_arr[i-1][j] + prefix_arr[i][j-1] - prefix_arr[i-1][j-1] + arr[i][j]
    
    # 파리채 구간 합 구해서 리스트에 넣기
    width_list = []
    for i in range(1, (N - M + 1) + 1):
        for j in range(1, (N - M + 1) + 1):
            x1, y1, x2, y2 = i, j, i + (M-1), j + (M-1)
            width = prefix_arr[x2][y2] - prefix_arr[x2][y1-1] - prefix_arr[x1-1][y2] + prefix_arr[x1-1][y1-1]
            width_list.append(width)
    '''
    횟수: (N - M + 1)**2
    앞 인덱스: 1부터 순서대로
    뒷 인덱스: i + (M-1)
    '''
    # 구간 합 리스트 내 최댓값 출력
    print(f'#{tc} {max(width_list)}')