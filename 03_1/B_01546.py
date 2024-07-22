N = int(input())  # 시험 본 과목의 개수
scores = list(map(int, input().split()))  # 시험 점수 리스트
M = max(scores)  # 시험 점수 중 최대값을 M에 할당

# 각 점수를 순회하며 최댓값으로 나눈 것에서 100을 곱한 결과를 리스트에 저장
adj = [score/M*100 for score in scores]  

# 바뀐 점수의 합을 점수의 개수로 나눔 (평균)
print(sum(adj)/len(adj))