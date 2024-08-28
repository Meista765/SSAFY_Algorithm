from heapq import heappush, heappop
 
T = int(input())
for test_case in range(1,T+1):
    N = int(input())
    arr = list(map(int,input().split()))
 
    heap = []   # 힙 리스트
 
 
    # 리스트 요소들을 하나씩 힙에 저장
    for i in range(N):
        heappush(heap,arr[i])
 
    S = 0
 
    # 마지막 노드부터 마지막 노드의 조상까지의 합
    #N-1 로 계산
    idx = N//2
    while idx >= 1:
        S += heap[idx-1]
        idx = idx//2
 
    print(f'#{test_case} {S}')