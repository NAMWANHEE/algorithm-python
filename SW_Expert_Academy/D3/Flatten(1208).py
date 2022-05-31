t = int(input())
for test in range(1,t+1):
    n = int(input())
    land = list(map(int,input().split()))
    for i in range(n):
        land.sort(reverse=True)
        land[0] = land[0]-1
        land[-1] = land[-1] +1
    land.sort(reverse=True)
    print('#'+str(test),land[0]-land[-1])