import sys
n,m = map(int,input().split())
num = []

for i in range(n):
    num.append(int(input()))
num.sort()

start, end = 0,0            # 시작과 마지막 투 포인터
ans = sys.maxsize           # 두수의 차이를 담는 변수, 초기값은 가장큰 경우인 20억보다 크게설정

while start < n and end < n:    # 시작과 마지막 포인터가 n보다 작을때 반복
    if num[end]-num[start] >= m:           # 두 수의 차가 m 보다 크다면
        ans = min(num[end]-num[start],ans) # 기존의 차이와 현재 차이중 작은 것으로 재설정
        start += 1                         # 시작 포인터 +1
    else:
        end += 1
print(ans)