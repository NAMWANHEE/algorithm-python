def solution(n, words):
    answer = []
    word = []  # 나온 단어 담을 리스트(단어리스트)
    num = 1  # 번호와 차례를 알기 위한 변수, 1번 사람부터 시작하므로 초기값 1
    for i in words:
        try:
            if i in word or word[-1][-1] != i[0]:  # 현재 나온 단어가 단어리스트에 있거나 이전 단어의 마지막 문자와 현재 단어의 시작 문자가 불일치 할 경우
                if num % n == 0:  # n명 중 마지막(n) 사람이 탈락한경우
                    answer.append(n)  # n번(번호) 추가
                    answer.append((num // n))  # [현재 단어의 번호를 n으로 나눈 몫 = 차례] 추가
                    break
                else:  # n명 중 마지막 사람을 제외한 나머지사람이 탈락한 경우
                    answer.append(num % n)  # num을 n으로 나눈 나머지(=번호) 추가
                    answer.append((num // n) + 1)  # 위에서 구한 방식에 +1 을 하여 차례 추가
                    break

            else:  # 현재 나온 단어 문제가 되지 않을 경우
                word.append(i)  # 단어리스트에 단어 추가
                num += 1  # 단어 번호 + 1
        except:
            word.append(i)
            num += 1

    if len(answer) == 0:  # 모든 단어가 문제 없을 경우
        answer.append(0)  # 0,0 추가
        answer.append(0)
    return answer