from collections import deque
t = int(input())
for i in range(t):
    word = deque(list(input()))
    flag = True

    if len(word) % 2 == 0:

        while word:
            a = word.popleft()
            b = word.pop()
            if a != b:
                flag = False
                break
        if flag == True:
            print('#'+str(i+1),1)
        else:
            print('#' + str(i + 1), 0)
    elif len(word) % 2 == 1:

        while len(word) != 1:
            a = word.popleft()
            b = word.pop()
            if a != b:
                flag = False
                break
        if flag == True:
            print('#'+str(i+1),1)
        else:
            print('#' + str(i + 1), 0)