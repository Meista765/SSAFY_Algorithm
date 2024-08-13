import sys
sys.stdin = open('C:/Users/SSAFY/Desktop/깃/SSAFY_Algorithm/SWEA/SWEA_11614_토너먼트/sample_input.txt', 'r')


## 힌트
# 최소값 구하기
# 문제를 시작, 끝 인덱스로 표현
# mid = (s + e) // 2
# s == e, arr[s] 가 답이다
# 그 외, min(min(s, mid), min(mid + 1, e))

## 토너먼트 카드 게임

arr = [60, 89, 39, 28, 49, 8, 16, 67, 11, 85]
# 최소값 구하기
# 문제를 시작, 끝 인덱스로 표현
# mid = (s + e) // 2
# s == e, arr[s]
# 그외, min(min(s, mid), min(mid + 1, e))
def find_min(s, e):
    if s == e:
        return s
    else:
        mid = (s + e) // 2
        lidx = find_min(s, mid)
        ridx = find_min(mid + 1, e)
        if arr[lidx] < arr[ridx]:
            return lidx
        return ridx

ret = find_min(0, len(arr) - 1)
print(ret, arr[ret])


