t = int(input())
for i in range(1,t+1):
    n = int(input())
    an = [[] for _ in range(n)]
    print('#'+str(i))
    for j in range(n):
        if j == 0:
            print(1)
            an[j].append(1)
            continue
        for k in range(j+1):
            if k == 0 or k == j:
                an[j].append(1)
            else:
                an[j].append(an[j-1][k-1]+an[j-1][k])
        print(*an[j])