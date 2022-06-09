from collections import Counter
t = int(input())
for test in range(1,t+1):
    n = list(input())

    if Counter(n)['o'] + (15-len(n)) >= 8:
        print('#'+str(test)+' YES')
    else:
        print('#'+str(test) + ' NO')