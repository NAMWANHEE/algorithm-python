import sys
from collections import defaultdict
n,m = map(int,input().split())
li =[]
for i in range(n):
    li.append(sys.stdin.readline().strip())
ans = ''
ans2 = 0
for i in range(m):
    dic = defaultdict(int)
    for j in range(n):
        dic[li[j][i]] += 1

    new = sorted(dic.items(), key=lambda x: x[0])
    new = sorted(new,key=lambda x:x[1],reverse=True)

    ans += new[0][0]
    if len(new) != 1:
        for k in range(1,len(new)):
            ans2 += new[k][1]

print(ans)
print(ans2)