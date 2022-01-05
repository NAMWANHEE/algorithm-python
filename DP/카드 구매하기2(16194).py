n = int(input())
dp = [0]+[10001] * n # n개의 인덱스 = n개 카드를 사는데 사용하는 최소 비용, 0번 인덱스는 0으로 나머지는 최대비용인 10000보다 큰 10001로 초기화
p =[0] + list(map(int,input().split())) # 각 개수 카드팩의 비용
dp[1] = p[1] # 카드 1개를 살때 최소 비용은 1개짜리 팩을 사는 비용


for i in range(2,n+1): # 점화식은 dp[i] = dp[i-j]+p[j] 로 나올수 있는 경우에 반복문을 돌며 dp[i]값에 들어가는 값중 작은 값으로 계속 갱신
    for j in range(1,i+1):
        dp[i] = min(dp[i],dp[i-j]+p[j])
print(dp[-1])