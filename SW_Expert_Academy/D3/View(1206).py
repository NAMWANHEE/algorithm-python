t = 10
for test in range(1,t+1):
    n = int(input())
    li = list(map(int,input().split()))
    ans = 0
    for i in range(2,n-2):
        m = max(li[i-1],li[i-2],li[i+1],li[i+2])
        if li[i] <= m:
            continue
        ans += li[i]-m
    print('#'+str(test),ans)