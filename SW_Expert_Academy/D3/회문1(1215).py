from collections import deque
def check(string):
    word = deque(string)
    flag = True
    if len(word) % 2 == 0:
        while word:
            a = word.popleft()
            b = word.pop()
            if a != b:
                flag = False
                break
        if flag == True:
            return 1
        else:
            return 0
    elif len(word) % 2 == 1:
        while len(word) != 1:
            a = word.popleft()
            b = word.pop()
            if a != b:
                flag = False
                break
        if flag == True:
            return 1
        else:
            return 0
for test in range(1,11):
    n = int(input())
    case = []
    for i in range(8):
        case.append(list(input()))
    answer = 0

    for i in range(len(case)):
        for j in range(len(case)-n+1):
            if check(case[i][j:j+n]) == 1:
                answer += 1

    for i in range(len(case)):
        for j in range(len(case)-n+1):
            st = ''
            for k in range(n):
                st += case[j+k][i]
            if check(st) == 1:
                answer += 1
    print('#'+str(test),answer)