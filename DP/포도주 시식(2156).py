li =[0]
dp = [0]
n = int(input())            # 포도주 잔의 개수
for i in range(n):          # 각 포도주 잔에 들어있는 포도주의 양
    li.append(int(input()))
if n == 1:                  # 포도주가 1개일 경우 최대 마실 수 있는 포도주의 양은 정해져있음
    dp.append(li[1])
elif n == 2:                # 포도주가 2개일경우도 1개일 경우와 마찬가지
    dp.append(li[1])
    dp.append(li[1]+li[2])

else:                       # 포도주가 3개이상일 경우
    dp.append(li[1])        # 포도주가 1,2 개일때 값을 dp 에 저장
    dp.append(li[1] + li[2])

    for i in range(3,n+1):
        dp.append(max(dp[i-1],li[i]+li[i-1]+dp[i-3],li[i]+dp[i-2]))
        # 현재 포도주를 선택하지 않고 바로이전까지의 최대 마실 수 있는 포도주의 양 = dp[i-1]과
        # 현재 포도주(li[i])와 바로 이전의 포도주(li[i-1])를 마시고 그 이전의 포도주(li[i-2])는 건너뛰고 그 이전의 포도주까지의 최대 마실수 있는 양 = dp[i-3]
        # 현재 포도주를 마시고 바로 이전 2개의 포도주를 마시지않고 그 이전의 포도주까지의 마실 수 있는 최대양 = dp[i-2]
        # 위의 3가지 경우중 가장 큰, 즉 가장 많이 마실 수 있는 것을 dp 에 추가
print(dp[-1]) # dp 리스트가 만들어지고 가장 dp의 마지막 값을 출력