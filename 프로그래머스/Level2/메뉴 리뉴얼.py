from itertools import combinations
from collections import defaultdict


def solution(orders, course):
    answer = []
    dic = defaultdict(int)

    for s in course:
        for i in orders:
            for j in combinations(i, s):
                dic[''.join(sorted(j))] += 1  # 각 코스별로 가능한 조합을 사전으로 표현

    count = []

    for s in course:
        max_num = 0
        for i in dic:
            if len(i) == s:  # 현재 메뉴의 길이가 코스 길이와 일치할 경우
                max_num = max(max_num, dic[i])  # 최대값(초기값=0)과 해당 메뉴의 주문 개수와의 최대값 계속 갱신
        count.append(max_num)  # 카운트리스트에 각 코스별 최대 최대조합의 개수 저장

    for i in range(len(count)):
        if count[i] == 1:  # 코스의 최대값이 1일 경우 제외
            continue
        for j in dic:  # 현재 메뉴의 갯수와 코스의 값이 같고 핸재 메뉴의 주문 갯수와 코스별 최대값과 동일한 경우
            if len(j) == course[i]:  # 정답 리스트에 해당 메뉴 추가
                if dic[j] == count[i]:
                    answer.append(j)

    return sorted(answer)