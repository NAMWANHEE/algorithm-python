from collections import defaultdict


def solution(s):
    answer = []
    dic = defaultdict(int)
    s = s.replace('{', '')  # 괄호 모두 제거
    s = s.replace('}', '')
    s = s.split(',')        # ',' 를 기준으로 나눔
    for i in s:             # 딕셔너리에 나온 횟수 카운트
        dic[i] += 1
    for i in sorted(dic.items(), key=lambda x: x[1], reverse=True): # 딕셔너리 value 값을 기준으로 정렬하여 가장 많이 나온 값부터 정답리스트에 추가
        answer.append(int(i[0]))

    return answer