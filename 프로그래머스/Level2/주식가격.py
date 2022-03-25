from collections import deque

def solution(prices):
    answer = []
    prices = deque(prices)  # 데크로 변경
    while True:
        now = prices.popleft()  # 현재 주식의 가격
        if len(prices) == 0:    # 주식 가격의 정보가 담긴 리스트가 비었을때 (마지막 값일 때)
            answer.append(0)    # 정답에 0추가 후 반복문 종료
            break
        count = 0               # 가격이 떨어지지 않은 초를 담을 변수
        for i in prices:
            if now <= i:        # 현재 주식 가격보다 크거나 같으면
                count += 1      # 카운트 + 1
            else:               # 현재 주식 가격보다 작으면
                count += 1      # 카운트 +1 해주고 반복문 종료
                break
        answer.append(count)    # 정답 (카운트 개수) 추가

    return answer