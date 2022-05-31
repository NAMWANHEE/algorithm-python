t = int(input())
for test in range(1,t+1):
    n = int(input())
    farm = []
    a = []
    idx = []
    for i in range(n):
        farm.append(list(map(int,list(input()))))

    b = 1
    c = 2
    c_idx = -1
    x = n//2
    for i in range(n):
        idx.append(x)
        a.append(b)
        if i == (n//2):
            c = -2
            c_idx = 1
        b += c
        x += c_idx

    answer = 0
    for i in range(n):
        for j in farm[i][idx[i]:idx[i]+a[i]]:
            answer += j
    print('#'+str(test),answer)