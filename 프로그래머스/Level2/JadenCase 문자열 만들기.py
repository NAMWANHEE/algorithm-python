def solution(s):
    answer = ''
    s = s.lower()     # 모든 문자 소문자로 변경
    s = s.split(' ')  # 공백을 기준으로 리스트로 만든다
    for i in s:
        try:
            if i[0].isdigit():      # 첫문자가 숫자일 경우
                answer += i + ' '   # 문자열 변경없이 그대로 정답 문자열에 추가
            else:                                    # 첫문자가 알파벳일 경우
                answer += i[0].upper() + i[1:] + ' ' # 가장 처음 알파벳의 대문자 + 2번째 문자부터 마지막 문자까지 더해준 문자열을 정답 문자열에 추가
        except:
            answer += ' '   # 현재 문자열이 공백인 경우 공백 추가

    return answer[:-1]  # 가장 마지막에 있는 공백 빼고 반환