t = int(input())
for test in range(1,t+1):
    n = int(input())
    li = list(map(int,input().split()))

    answer = [0]
    for i in li:
        answer = list(set(answer))
        for j in range(len(answer)):
            answer.append(answer[j] + i)
    print('#'+str(test),len(set(answer)))