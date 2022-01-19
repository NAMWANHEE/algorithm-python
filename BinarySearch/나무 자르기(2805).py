a,b = map(int,input().split())
n = list(map(int,input().split()))
left,right = 1,max(n) # left: 가장짧은 나무의 길이, right: 가장긴 나무의 길이

while left <= right:
    mid = (left+right) // 2  # 자를 톱의 높이 설정
    meter = 0                # 자르고 가져갈 수 있는 나무의 미터
    for i in n:              # 반복문을 돌며 나무가 톱의 높이 보다 클경우
        if i > mid:          # (현재 나무높이 - 톱의 높이)값을 현재 가지고 있는 나무의 미터와 더하여 갱신
            meter += i-mid
            if meter >= b:   # 자른 나무의 길이가 b 이상이면 더이상 반복 X
                break
    if meter >= b:           # 자른 나무의 길이가 b 이상일 때
        left = mid+1         # 가장 짧은 나무의 길이를 톱의 높이(mid) +1 한값으로 설정
    else:                    # 자른 나무의 길이가 b 미만일 때
        right = mid-1        # 가장 긴 나무의 길이를 톱의 높이(mid) -1 값으로 설정
print(right)