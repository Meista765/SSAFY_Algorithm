arr = [1, 2, 3]
N = len(arr)
visit = [0] * N  # 요소의 선택 여부 저장
order = [0] * N  # 실제 순열의 순서를 저장

# =============================================
# 1. 반복 구조
for i in range(N):      # 첫번째 요소 선택
    if visit[i]: continue
    order[0] = arr[i]
    visit[i] = 1
    #----------------------------------------------
    for j in range(N):  # 두번째 요소 선택
        if visit[j]: continue
        order[1] = arr[j]
        visit[j] = 1
        #------------------------------------------
        for k in range(N): # 세번째 요소 선택
            if visit[k]: continue
            order[2] = arr[k]
            visit[k] = 1
            print(order)
            visit[k] = 0
        #------------------------------------------
        visit[j] = 0
    #------------------------------------------
    visit[i] = 0

# =============================================
# 2. 재귀 구조
def perm(k, N):
    if k == N:
        print(order)
    else:
        for i in range(N):  # 첫번째 요소 선택
            if visit[i]: continue
            order[k] = arr[i]
            visit[i] = 1
            #---------------------
            perm(k + 1, N)
            #---------------------
            visit[i] = 0
perm(0, N)
