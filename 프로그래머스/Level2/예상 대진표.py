def solution(n, a, b):
    answer = 1

    while True:
        if abs(a - b) == 1 and (a // 2) != (b // 2):    # 두 참가자의 번호의 차이가 1이면서 두번호를 2로 각각 나눈 몫이 같지 않을 때(마지막 라운드) 종료
            break
        if a % 2 == 0:          # a 참가자 번호가 2로 나누어떨어지면
            a = int(a / 2)      # a 참가자의 번호를 2로 나눈값으로 재설정
        else:
            a = int(a / 2) + 1  # 2로 나누어 떨어지지 않으면 2로 나눈값에 +1 한 값으로 재설정

        if b % 2 == 0:          # a 참가자와 마찬가지로 b 참가자도 재설정
            b = int(b / 2)
        else:
            b = int(b / 2) + 1
        answer += 1             # 카운트 + 1
    return answer
