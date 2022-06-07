t = int(input())
for test in range(1,t+1):
    n = int(input())
    length = len(str(n))
    dic1 = {}
    if length == 1:
        print('#'+str(test)+' impossible')
        continue
    for i in str(n):
        dic1[i] = 1

    num = 2
    while True:
        dic2 = {}
        if len(str(n*num)) > length:
            print('#'+str(test)+' impossible')
            break
        for i in str(n*num):
            dic2[i] = 1
        if dic1 == dic2:
            print('#'+str(test)+' possible')
            break
        num += 1