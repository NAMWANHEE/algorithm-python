n = int(input())
li = list(map(int,input().split()))
dp = [0] * n
dp[0] = li[0] # dp의 첫번째 값 = 주어진 수열의 첫번째 값
for i in range(1,n):                  # dp의 1번부터 채워나감, dp는 현재수열까지중 최대값만 저장
    dp[i] = max(li[i],li[i]+dp[i-1])  # 현재값과 (이전까지의 수열의 최대연속합+현재값)을 비교하여 더 큰값을 dp에 저장

print(max(dp)) # dp 리스트중 가장큰 값을 출력력