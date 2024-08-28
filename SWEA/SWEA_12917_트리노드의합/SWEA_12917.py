import sys
sys.stdin = open('C:/Users/SSAFY/Desktop/git/SSAFY_Algorithm/SWEA/SWEA_12917_트리노드의합/sample_input.txt', 'r')

T = int(input())

for tc in range(1, T + 1):
    N, M, node = map(int, input().split())
    # 트리
    arr = [0] * (N + 1)
    
    for _ in range(M):
        # 노드 번호에 값 넣기
        c, value = map(int, input().split())
        arr[c] = value
        
        # 조상 노드들에 더해주기
        while True:
            c //= 2
            arr[c] += value
            if c == 1:
                break
    
    print(f'#{tc} {arr[node]}')