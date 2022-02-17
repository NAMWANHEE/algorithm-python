def solution(answers):
    answer = []
    one = [1,2,3,4,5]              # 1번 수포자
    two = [2,1,2,3,2,4,2,5]        # 2번 수포자
    three = [3,3,1,1,2,2,4,4,5,5]  # 3번 수포자
    a,b,c = 0,0,0                  # 1,2,3번이 맞춘 개수

    for i in range(len(answers)):
        if answers[i] == one[i % 5]:    # 1번 => i번 정답 = 수포자의 i%5 번째 답이 맞으면 카운트
            a += 1
        if answers[i] == two[i % 8]:    # 2번 => i번 정답 = 수포자의 i%8 번째 답이 맞으면 카운트
            b += 1
        if answers[i] == three[i % 10]: # 3번 => i번 정답 = 수포자의 i%10 번째 답이 맞으면 카운트
            c += 1

    ma = max(a,b,c)     # 3개중 최대 정답 개수

    if ma == a:         # a 가  최대값이면 1번 수포자 추가
        answer.append(1)
    if ma == b:         # b 가  최대값이면 2번 수포자 추가
        answer.append(2)
    if ma == c:         # c 가  최대값이면 3번 수포자 추가
        answer.append(3)
    return answer