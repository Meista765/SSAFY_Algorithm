import sys
sys.stdin = open('input.txt')

T = int(input())
for test_case in range(1,T+1):
    N, M = map(int, input().split())     # N: 컨테이너 수, M: 트럭 수
    W = sorted(list(map(int, input().split())),reverse=True)  # 컨테이너의 무게
    T = sorted(list(map(int, input().split())),reverse=True)  # 트럭의 적재용량

    total = 0

    idx = 0
    for i in range(M):
        while idx < N:
            if T[i] >= W[idx]:
                total += W[idx]
                idx += 1
                break
            idx += 1
        else:
            break
    print(f'#{test_case} {total}')


