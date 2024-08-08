import sys;
sys.stdin = open('4835.txt')

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))

    m_sum = 0
    for i in range(M):
        m_sum += arr[i]

    min_sum = m_sum
    max_sum = m_sum

    for e in range(M, N):
        m_sum += arr[e] - arr[e - M]

        if min_sum > m_sum:
            min_sum = m_sum

        if max_sum < m_sum:
            max_sum = m_sum

    print(f'#{tc} {max_sum - min_sum}')
