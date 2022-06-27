from itertools import permutations
n = int(input())
li = list(map(int,input().split()))
leng = len(li)
new_li = list(permutations(li))
ans = 0
for i in new_li:
    m = 0
    for j in range(leng-1):
        m += abs(i[j]-i[j+1])
    ans = max(m,ans)
print(ans)