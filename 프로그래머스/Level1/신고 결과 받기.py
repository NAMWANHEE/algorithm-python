from collections import defaultdict
def solution(id_list, report, k):
    answer = []
    a = {}  # 신고한 사람 = [신고당한사람]
    b = {}  # 신고당한 사람 = [신고한사람]
    mail = [] # 신고를 k 번 이상 당한 사람의 리스트
    for i in id_list: # 각 사전의 value 값들을 리스트로 만들어줌
        a[i] = []
        b[i] = []

    for i in report:
        if i.split(' ')[1] in a[i.split(' ')[0]]:   # 중복 신고 제거하는 부분
            continue
        a[i.split(' ')[0]].append(i.split(' ')[1])

    for i in report:
        if i.split(' ')[0] in b[i.split(' ')[1]]:
            continue
        b[i.split(' ')[1]].append(i.split(' ')[0])

    # line 11~19 와 동일한 코드, set을 이용해 중복을 없애고 반복문을 하면 더 편리한듯.
    # for i in set(report):
    #     a[i.split(' ')[0]].append(i.split(' ')[1])
    #     b[i.split(' ')[1]].append(i.split(' ')[0])

    for i in b:
        if len(b[i]) >= k:  # k번이상 신고당한 경우
            mail.append(i)  # mail 리스트에 이름 추가

    for i in a.values(): # 신고한 사람 = [신고당한사람] => 신고당한 사람의 리스트를 반복하여 k번이상 신고 당한 사람인지 체크
        c = 0
        for j in i:
            if j in mail: # mail 리스트에 있으면 k번이상 신고당했기 때문에 카운트 +1
                c += 1
        answer.append(c)  # 정답 리스트에 카운트한 값 추가
    print(answer)
    return answer