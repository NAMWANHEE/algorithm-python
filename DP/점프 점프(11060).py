n = int(input())
li = list(map(int,input().split()))

dp = [1001 for _ in range(n)]
dp[0] = 0
for i in range(n):
    for j in range(1,li[i]+1):
        try:
            dp[i+j] = min(dp[i]+1,dp[i+j])
        except:
            continue
if dp[-1] == 1001:
    print(-1)
else:
    print(dp[-1])