n,k = map(int,input().split())
li = list(map(int,input().split()))
ans = []
m = -999999999
for i in range(n-k+1):
    m = max(m,sum(li[i:i+k]))
print(m)