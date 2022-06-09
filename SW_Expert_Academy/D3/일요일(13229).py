t = int(input())
day = ['SUN','MON','TUE','WED','THU','FRI','SAT']
for test in range(1,t+1):
    n = input()
    s = day.index(n)
    print('#'+str(test),7-s)