def solution(n):
    ans = 0

    while n != 0:  # 거리(n)이 0이 되면 반복문 종료
        if n % 2 == 0:  # 거리가 2로 나누어떨어진다면
            n = int(n / 2)  # 카운트 하지않고 이동
        else:  # 거리가 2로 나누어떨어지지 않으면
            ans += 1  # 한 칸 점프 (카운트)
            n = n - 1  # 거리는 한 칸 점프하므로 1 줄어듬

    return ans