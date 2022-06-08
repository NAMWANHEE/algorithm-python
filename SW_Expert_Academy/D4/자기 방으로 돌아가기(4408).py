from collections import deque
t = int(input())
for test in range(1,t+1):
    n = int(input())
    info = deque()
    for i in range(n):
        info.append(list(map(int,input().split())))
    visit = [0] * 200
    for j in info:
        if j[0] > j[1]:
            a = (j[1]-1) //2
            b = (j[0]-1) // 2
        else:
            b = (j[1] - 1) // 2
            a = (j[0] - 1) // 2
        for k in range(a,b+1):
            visit[k] += 1

    print('#'+str(test),max(visit))