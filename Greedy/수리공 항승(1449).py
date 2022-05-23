n,m = map(int,input().split())
li = list(map(int,input().split()))
li.sort()
now = 0
ans = 0
for i in li:
    if i <= now:
        continue
    else:
        now = i + m -1
        ans += 1
print(ans)