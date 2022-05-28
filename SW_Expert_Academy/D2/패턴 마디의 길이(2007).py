from collections import deque
t = int(input())
for i in range(t):
    word = deque(list(input()))
    compare = []
    for j in range(len(word)):
        compare.append(word.popleft())
        a = len(compare)

        if compare == list(word)[:a]:
            print('#'+str(i+1),len(compare))
            break