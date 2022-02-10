import sys
d,n = map(int,input().split())
oven = list(map(int,input().split())) # 오븐의 사이즈(맨위 -> 맨아래)
dow = list(map(int,input().split()))  # 피자 반죽의 크기

for i in range(1,d):
    oven[i] = min(oven[i],oven[i-1])  # 오븐의 크기가 현재위치가 아무리 커도 바로 위의 오븐크기가 작으면 소용이 없으므로
                                      # 현재위치의 오븐과 위의 오븐 크기를 비교하여 작은것으로 바꿔준다
now = 0                               # 도우 선택을 위한 인덱스
ans = 0                               # 정답 위치
for i in reversed(range(d)):          # 맨아래 오븐 크기부터와 비교
    if oven[i] >= dow[now]:           # 오븐크기가 반죽보다 크면
        now += 1                      # 다음 도우
        ans = i+1                     # 현재 도우가 있는 오븐의 위치
    if now >= n:                      # 도우를 모두 사용한 경우 정답 출력 후 시스템 종료
        print(ans)
        sys.exit(0)
print(0)                              # 피자가 모두 오븐에 들어가지 않는 경우 -> 0출력