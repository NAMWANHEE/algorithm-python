n,s = map(int,input().split())
li = list(map(int,input().split()))
left = 0     # 왼쪽 가르키는 포인터
right = 0    # 오른쪽 가르키는 포인터
a_sum = 0    # 두 포인터사이의 값 = 구간합
ans = 100001 # 정답담을변수, n의 값이 10~100000 이므로 가장큰 100000일경우 보다 1 큰 값

while True:
    if a_sum >= s:                 # 두 포인터사이의 값이 기준값(s) 이상일 경우
        ans = min(ans,right-left)  # 이전의 정답(최소 길이)와 지금 (오른쪽 포인터-왼쪽 포인터) 값 중 작은 값을 정답으로 변경
        a_sum -= li[left]          # 구간합에 왼쪽이 가르키는 포인터의 값 -
        left += 1                  # 왼쪽 포인터를 1칸 왼쪽으로 이동

    elif right == n:               # 오른쪽을 가르키는 포인터가 마지막일 경우
        break

    else:
        a_sum += li[right]         # 현재 오른쪽 포인터가 가르키는 위치의 값 +
        right += 1                 # 오른쪽 포인터를 1칸 오른쪽으로 이동


if ans == 100001:                  # 구간합이 기준값(s) 이상인 경우가 없는 경우 0 출력
    print(0)
else:
    print(ans)