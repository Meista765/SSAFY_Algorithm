n = int(input())
m = int(input())

unique_number_list = list(map(int,input().split()))
unique_number_list.sort()

start_index = 0
end_index = n-1
cnt = 0

while start_index < end_index: 
    if unique_number_list[start_index] + unique_number_list[end_index] == m:
        cnt += 1
        start_index += 1
    
    elif unique_number_list[start_index] + unique_number_list[end_index] > m:
        end_index -= 1
    
    else:
        start_index +=1 

print(cnt)


# 답안지를 보고 추가적으로 알게 된 사실

## 같아졌을 때, start_index만 오른쪽으로 한칸 이동하는 것이 아닌 end_index도 왼쪽으로 한칸 이동한다.
## 이유는 아마도 문제에서 고유한 번호라고 했기 때문에 중복된 값이 없어서 일지 아닐까 생각이 듭니다.


