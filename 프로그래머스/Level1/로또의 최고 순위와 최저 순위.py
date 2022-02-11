def solution(lottos, win_nums):
    answer = []
    big = 0 # 0이 주어진 경우 당첨됐다고 가정하에 카운트
    a = [] # 최고 순위 번호와 최저 순위 번호 담을 리스트
    c = 0  # 주어진 번호에서 당첨된 번호 카운트
    for i in lottos:
        if i in win_nums: # 가지고있는 로또중 당첨 번호안에 있으면
            c += 1        # 카운트 +1
        elif i == 0:      # 번호가 0이면 당첨됐다고 가정하고 big 카운트 +1
            big += 1
    a.append(big+c)       # 최고 순위 번호 추가
    a.append(c)           # 최저 순위 번호 추가
    for i in a:
        if i == 6:          # 당첨번호가 6개면 1등 , 5개면 2등 .....2개면 5등 나머지는 6등
            answer.append(1)
        elif i == 5:
            answer.append(2)
        elif i == 4:
            answer.append(3)
        elif i == 3:
            answer.append(4)
        elif i == 2:
            answer.append(5)
        else:
            answer.append(6)
    return answer