t = int(input())
for c in range(t):
    m,n = map(int,input().split())
    bug = []
    for i in range(m):
        bug.append(list(map(int,input().split())))
    ans = []
    for i in range(m-n+1):
        for j in range(m-n+1):
            sum1 = 0
            for k in range(n):
                sum1 += sum(bug[i+k][j:j+n])
            ans.append(sum1)
    print('#'+str(c+1),max(ans))