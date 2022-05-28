from collections import defaultdict
t = int(input())
for test in range(1,t+1):
    n = int(input())
    dic = defaultdict(int)
    number = list(map(int,input().split()))

    for i in number:
        dic[i] += 1
    sort_dic = sorted(dic.items(), key=lambda x: x[0], reverse=True)
    sort_dic = sorted(sort_dic, key =lambda x: x[1], reverse= True)
    print('#'+str(test),sort_dic[0][0])