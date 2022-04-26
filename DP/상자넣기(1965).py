n = int(input())
box = list(map(int,input().split()))

dp = [1] * n

for i in range(1,n):
    idx = i
    while idx != 0:
        if box[i] > box[idx-1]: # 현재 인덱스 이전의 위치의 값보다 현재 값이 큰 경우
            dp[i] = max(dp[i],dp[idx-1] + 1) # 현재 상자의 개수와 이전 인덱스의 상자 개수+1 값중 큰 값으로 갱신
            idx -= 1    # 인덱스 1 빼기
        else:
            idx -= 1
print(max(dp)) # 최대 상자 개수 출력
