n = int(input())
dp = [0] * (n+1) # n개의 인덱스 = n개 카드를 사는데 사용하는 최대 비용
p =[0] + list(map(int,input().split())) # 각 개수 카드팩의 비용
dp[1] = p[1] # 카드 1개를 살때 최대 비용은 1개짜리 팩을 사는 비용

for i in range(2,n+1): # 점화식은 dp[i] = dp[i-j]+p[j] 로 나올수 있는 경우에 대해 가장 큰값을 dp 리스트에 저장
    for j in range(1,i+1):
        if dp[i] < dp[i-j]+p[j]:
            dp[i] = dp[i-j]+p[j]
print(dp[-1])