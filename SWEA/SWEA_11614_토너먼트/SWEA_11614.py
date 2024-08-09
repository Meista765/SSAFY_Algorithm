import sys
sys.stdin = open('C:/Users/SSAFY/Desktop/git/SSAFY_Algorithm/SWEA/SWEA_11614_토너먼트/sample_input.txt', 'r')


## 힌트
# 최소값 구하기
# 문제를 시작, 끝 인덱스로 표현
# mid = (s + e) // 2
# s == e, arr[s] 가 답이다
# 그 외, min(min(s, mid), min(mid + 1, e))

arr = [60, 89, 39, 28, 49, 8, 16, 67, 11, 85]
def find_min(s, e):
    if s == e:
        return arr[s]
    else:
        mid = (s + e) // 2
        lmin = find_min(s, mid)
        rmin = find_min(mid + 1, e)
        if arr[lmin] < arr[rmin]:
            return arr[lmin]
        return arr[rmin]

ret = find_min(0, len(arr) - 1)
print(ret)


