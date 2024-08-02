# 시간 초과
# 무엇이 문제일까 
# 투포인트를 제대로 구현하지 못함

'''
s, p = map(int,input().split()) # s는 DNA 문자열의 길이, p는 부분 문자열의 길이
string = input()
check_list = list(map(int, input().split())) # A, C, G, T의 최소 개수

check_dict = {k:v for k,v in zip(['A','C','G','T'],check_list)}




my_dict = {'A':0, 'C':0, 'G':0, 'T':0}

start_index = 0
end_index = p-1
result = 0
while end_index < s:
    cnt = 0

    #print(string[start_index:end_index+1])
    my_dict['A'] = string[start_index:end_index+1].count('A')
    my_dict['C'] = string[start_index:end_index+1].count('C')
    my_dict['G'] = string[start_index:end_index+1].count('G')
    my_dict['T'] = string[start_index:end_index+1].count('T')
    # print(my_dict)

    for k in my_dict.keys():
        if my_dict[k] >= check_dict[k]:
            cnt += 1
    
    if cnt ==4:
        result += 1

    start_index +=1
    end_index += 1
    # print(f'end_index:{end_index}')
    
print(result)

'''
# 이 방식은 다시 도전해보자
'''s, p = map(int,input().split()) # s는 DNA 문자열의 길이, p는 부분 문자열의 길이
string = input()
check_list = list(map(int, input().split())) # A, C, G, T의 최소 개수

check_dict = {k:v for k,v in zip(['A','C','G','T'],check_list)}

my_dict = {'A':0, 'C':0, 'G':0, 'T':0}

start_index = 0
end_index = p-1
result = 0

def my_add(c):
    global my_dict
    my_dict[c] += 1

def my_substrack(c):
    global my_dict
    my_dict[c] -= 1

# 초기 값 설정

my_dict['A'] = string[start_index:end_index+1].count('A')
my_dict['C'] = string[start_index:end_index+1].count('C')
my_dict['G'] = string[start_index:end_index+1].count('G')
my_dict['T'] = string[start_index:end_index+1].count('T')
cnt = 0
# for k in my_dict.keys():
#     if my_dict[k] >= check_dict[k]:
#         cnt += 1
    
#     if cnt == 4:
#         result += 1




for s in string: 
    my_add(s)
    my_substrack(s)

    for k in my_dict.keys():
        cnt = 0
        if my_dict[k] >= check_dict[k]:
            cnt += 1

        if cnt == 4:
            result +=1 

'''
s, p = map(int,input().split()) # s는 DNA 문자열의 길이, p는 부분 문자열의 길이
string = input()
check_list = list(map(int, input().split())) # A, C, G, T의 최소 개수

result = 0 # 가능한 키 갯수
start_index = 0
end_index = p-1

my_dict = {'A':0, 'C':0, 'G':0, 'T':0}

check_dict = {k:v for k,v in zip(['A','C','G','T'],check_list)} 

# 초기 값 설정

my_dict['A'] = string[start_index:end_index+1].count('A')
my_dict['C'] = string[start_index:end_index+1].count('C')
my_dict['G'] = string[start_index:end_index+1].count('G')
my_dict['T'] = string[start_index:end_index+1].count('T')

def my_add(k):       # 새로운 문자가 들어오면 현재 딕셔너리에서 해당 문자 count +1
    global my_dict
    my_dict[k] += 1

def my_sustrack(k): # 새로운 문자가 들어오면 이전 start_index에 해당하는 문자 count -1
    global my_dict
    my_dict[k] -= 1

while True:
    for k in my_dict.keys():
        if my_dict[k] < check_dict[k]:
            break
    else:
        result += 1

    
    
    start_index += 1 # start_index 한칸 이동
    end_index += 1 # end_index 한칸 이동
    
    if end_index > s-1: # end_index가 문자열의 길이를 벗어날 때 while 탈출
        break
    # 새로운 문자열을 받아 함수 적용
    my_add(string[end_index]) 
    my_sustrack(string[start_index -1])

print(result)









    
    


