n = int(input())
ans = list(map(int,input().split()))

dp = [1] * n

for i in range(len(ans)):
    for j in range(i):
        if ans[i] > ans[j]:
            dp[i] = max(dp[i],dp[j]+1)
print(max(dp))