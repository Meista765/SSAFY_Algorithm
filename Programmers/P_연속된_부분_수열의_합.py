def solution(sequence:list, k:int):
    answer = [0, 0]
    
    # 부분합을 저장하는 변수
    S = [0]
    
    # 부분합 계산
    tmp = 0
    for element in sequence:
        tmp += element
        S.append(tmp)
    
    # 투-포인터로 정답 탐색 (i: start, j: end)
    i = 0
    j = 1
    diff = 1000000000
    
    while i <= j and j <= len(sequence):
        # 부분합이 k와 동일하면, 정답 갱신
        if S[j] - S[i] == k and (j-i < diff):
            answer = [i, j-1]
            diff = j-i
            j += 1
        elif S[j] - S[i] < k:
            j += 1
        else: # S[j] - S[i] > k
            i += 1
    
    return answer