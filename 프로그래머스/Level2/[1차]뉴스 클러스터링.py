from collections import Counter


def solution(str1, str2):
    str1 = str1.upper()  # 두개의 입력 문자열을 모두 소문자 or 대문자 둘중 하나로 변환
    str2 = str2.upper()

    s1 = []
    s2 = []

    for i in range(len(str1) - 1):  # 1번문자열을 2개씩 끊은 문자열이 알파벳일 경우만 s1에 추가
        if str1[i:i + 2].isalpha():
            s1.append(str1[i:i + 2])
    for i in range(len(str2) - 1):  # 2번문자열을 2개씩 끊은 문자열이 알파벳일 경우만 s2에 추가
        if str2[i:i + 2].isalpha():
            s2.append(str2[i:i + 2])

    s1 = Counter(s1)  # Counter 적용
    s2 = Counter(s2)

    up = (s1 & s2).elements()  # 두 리스트의 교집합 요소
    down = (s1 | s2).elements()  # 두 리스트의 합집합 요소

    a = len(list(up))  # 교집합의 갯수
    b = len(list(down))  # 합집합의 갯수
    try:
        answer = int(a / b * 65536)  # 자카드 유사도의 식에 따라 교집합/합집합*65536 을 소수는 버리고 정수만 남김

    except:
        answer = 65536  # 예외 처리

    return answer