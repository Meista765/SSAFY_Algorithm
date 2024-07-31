import sys
input = sys.stdin.readline

checkList = [0] * 4
myList = [0] * 4
checkSecret = 0

def myadd(str):
    global checkList, myList, checkSecret
    if str == 'A':
        myList[0] += 1
        if myList[0] == checkList[0]:
            checkSecret += 1

    elif str == 'C':
        myList[1] += 1
        if myList[1] == checkList[1]:
            checkSecret += 1

    elif str == 'G':
        myList[2] += 1
        if myList[2] == checkList[2]:
            checkSecret += 1

    else:
        myList[3] += 1
        if myList[3] == checkList[3]:
            checkSecret += 1

def myremove(str):
    global checkList, myList, checkSecret
    if str == 'A':
        myList[0] -= 1
        if myList[0] < checkList[0]:
            checkSecret -= 1

    elif str == 'C':
        myList[1] += 1
        if myList[1] < checkList[1]:
            checkSecret -= 1

    elif str == 'G':
        myList[2] += 1
        if myList[2] < checkList[2]:
            checkSecret -= 1

    else:
        myList[3] += 1
        if myList[3] < checkList[3]:
            checkSecret -= 1

S, P = map(int, input().split())
result = 0
A =  input()
checkList = list(map(int, input().split()))

for i in range(len(checkList)):
    if checkList[i] == 0:
        checkSecret += 1

for i in range(P):
    myadd(A[i])
if checkSecret == 4:
    result += 1

for i in range(P, S):
    j = i - P
    myadd(A[i])
    myremove(A[j])
    if checkSecret == 4:
        result += 1

print(result)

