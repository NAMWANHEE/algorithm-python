from collections import defaultdict
import copy


def solution(n, results):
    answer = 0
    win = defaultdict(set)  # '선수 번호' : {'해당 선수가 이긴 선수 목록'}
    lose = defaultdict(set)  # '선수 번호' : {'해당 선수가 진 선수 목록 '}
    for i in results:
        win[i[0]].add(i[1])
        lose[i[1]].add(i[0])

    for i in range(1, n + 1):  # 1번 선수부터 n번 선수까지 반복
        for j in lose[i]:  # i번 선수를 이긴 선수 j
            win[j].update(win[i])  # j번 선수는 i번 선수가 이긴 선수들 모두를 이길 수 있다
        for s in win[i]:  # 위와 마찬가지로 지는 경우 추가
            lose[s].update(lose[i])

    for i in range(1, n + 1):  # 해당 선수가 이기고 지는 선수들의 총합이 n-1 과 같다면 정답 +1 추가
        if len(win[i]) + len(lose[i]) == n - 1:
            answer += 1
    return answer
