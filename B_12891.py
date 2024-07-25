s, p = map(int,input().split()) # s는 DNA 문자열의 길이, p는 부분 문자열의 길이
string = input()
minimum = list(map(int, input().split())) # A, C, G, T의 최소 개수

start_index = 0
end_index = p-1
cnt = 0 # 갯수 카운트

now_list =[0] * 4
while end_index < s:
    now_list =[0] * 4
    for s in string[start_index:end_index+1]:
        if s == 'A':
            now_list[0] += 1
        elif s == 'C':
            now_list[1] += 1
        elif s == 'G':
            now_list[2] += 1
        elif s == 'T':
            now_list[3] += 1

    for i in range(4):
        if now_list[i] < minimum[i]:
            break
    else:
        cnt += 1

print(cnt)


            





