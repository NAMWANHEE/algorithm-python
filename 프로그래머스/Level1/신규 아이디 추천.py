import string
from collections import deque

def solution(new_id):
    answer = ''
    li = ['-', '_', '.', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    li.extend([i for i in string.ascii_lowercase])
    new_id = new_id.lower() # 1단계 모든 대문자를 소문자로 치환
    new = deque()           # 규정된 문자담을 리스트
    for i in new_id:
        if i in li:         # 규정된 문자에 포함되는 문자일경우
            try:
                if new[-1] == '.' and i == '.': # '.' 이 연속되는 경우 다음 반복문 실행
                    continue
            except:
                pass
            new.append(i)       # 위의 조건이 만족하면 new 리스트에 추가
    try:
        if new[0] == '.':       # 맨앞이 '.' 인경우 삭제
            new.popleft()
        elif new[-1] == '.':    # 맨뒤가 '.' 인경우 삭제
            new.pop()
    except:
        pass
    new = list(new)             # deque -> list로 변환 (슬라이싱하기위해)

    if len(new) == 0:           # 5단계 빈 문자열일 경우 'a' 추가
        new.append('a')
    if len(new) >= 16:          # 6단계 문자열의길이가 16이상인경우 처음 15개의 문자만 남겨둠
        new = new[:15]
    if new[-1] == '.':          # 15개만 남겨두고 맨뒤에가 '.' 인 경우 '.' 제거
        new.pop()

    while len(new) < 3:         # 7단계 문자길이가 2이하인 경우 기존 문자의 마지막 문자를 길이가 3이 되도록 만들어줌
        new.append(new[-1])
    for i in new:               # 생성된 문자 리스트를 정답 문자열로 만들어줌줌
       answer += i
    return answer