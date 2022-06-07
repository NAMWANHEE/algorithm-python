t = int(input())
for test in range(1,t+1):
    n,d = map(int,input().split())
    range_d = d*2 + 1
    if n % range_d == 0:
        print('#'+str(test),n//range_d)
    else:
        print('#' + str(test), n // range_d + 1)