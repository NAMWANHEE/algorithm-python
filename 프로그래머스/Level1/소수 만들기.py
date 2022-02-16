def solution(nums):
    def sol(x):                                 # x가 소수라면 True, 소수가 아니라면 False 를 반환하는 함수
        for i in range(2, int(x ** 0.5) + 1):   # x의 제곱근까지만 반복하여 시간 단축
            if x % i == 0:
                return False
        return True

    answer = 0

    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            for k in range(j + 1, len(nums)):        # 3개의 숫자를 뽑기때문에 반복문 3개
                if sol(nums[i] + nums[j] + nums[k]): # 뽑은 3개의 숫자를 위의 함수에 넣어 소수일경우
                    answer += 1                      # 정답 카운트 +1

    return answer