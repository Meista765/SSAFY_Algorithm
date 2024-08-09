arr = [1, 2, 3]
N = len(arr)
visit = [0] * N  # 요소의 선택 여부 저장
order = [0] * N  # 실제 순열의 순서를 저장
a = []

def perm(k, N):
    global a
    if k == N:
        a.append(order[:])

    else:
        for i in range(N):  # 첫번째 요소 선택
            if visit[i]: continue
            order[k] = arr[i]
            visit[i] = 1
            #a.append(arr[i])
            #---------------------
            perm(k + 1, N)
            #---------------------
            visit[i] = 0
            #a.pop()

perm(0,N)
print(a)

