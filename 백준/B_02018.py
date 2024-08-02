# 첫 풀이 결과 -> 메모리 초과
'''
N = int(input())

number_list = list(range(1,N+1))
start_index = 0
end_index = 0
cnt = 1 # 가짓 수 카운트 , 초기 값이 1인 이유는 N을 먼저 뽑는 경우의 수를 미리 넣고 시작하기 때문

number_sum = number_list[start_index] # 초기값 설정


while start_index != N-1:
     
    if number_sum < N:    # 연속된 자연수의 합이 N보다 작으면 start_index 오른쪽으로 한칸 이동
        
        start_index += 1
        number_sum += number_list[start_index]

    elif number_sum == N: # 연속된 자연수의 합이 N과 같다면 cnt 1증가 및 start_index 오른쪽으로 한칸 이동
        cnt += 1
        start_index += 1
        number_sum += number_list[start_index]
        # print(start_index-1,end_index)확인용
    else:                 # 연속된 자연수의 합이 N보다 크다면 end_index 오른쪽으로 한칸 이동
        number_sum -= number_list[end_index]
        end_index +=1
# print(start_index,end_index)확인용
print(cnt)
        
'''        

# 2 try -> 리스트 안쓰고
N = int(input())

start_index = 1
end_index = 1
cnt = 1 # 가짓 수 카운트
number_sum = 1 

while start_index != N:
        if number_sum < N:    # 연속된 자연수의 합이 N보다 작으면 start_index 오른쪽으로 한칸 이동
            start_index += 1
            number_sum += start_index
        
        elif number_sum == N: # 연속된 자연수의 합이 N과 같다면 cnt 1증가 및 start_index 오른쪽으로 한칸 이동
            cnt += 1
            start_index += 1
            number_sum += start_index
        
        else:                # 연속된 자연수의 합이 N보다 크다면 end_index 오른쪽으로 한칸 이동
            number_sum -= end_index
            end_index += 1

print(cnt)



