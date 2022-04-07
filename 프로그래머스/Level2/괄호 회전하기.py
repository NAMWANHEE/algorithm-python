def solution(s):
    answer = 0
    count = len(s)
    if len(s) < 2:
        return 0
    while count != 0:       # 문자열 길이 만큼 반복
        if check(s) == 0:
            pass
        else:               # 완전한 문자열이면 + 1 추가 아니라면 pass
            answer += 1
        s = s[1:] + s[0]    # 맨 왼쪽 문자 하나를 맨 오른쪽으로 이동
        count -= 1
    return answer

a = {1: '[', 2: '(', 3: '{'}
b = {1: ']', 2: ')', 3: '}'}
def check(c):                               # 주어진 문자열이 올바른 괄호 문자열인지 체크하는 함수
    stack = []
    for i in c:
        if stack:                           # 스택에 문자가 들어있으면
            if i in a.values():             # 현재 문자가 '[','(','{' 중 하나라면 스택에 추가
                stack.append(i)
            else:                           # 현재 문자가 ], ), } 중 하나라면
                if i == b[1]:               # ] 일때 스택의 마지막 문자가 [ 라면 pop
                    if stack[-1] == a[1]:   # 아니라면 스택에 현재 문자 추가
                        stack.pop()         # 위와 동일한 방식으로 ), } 모두 해줌
                    else:
                        stack.append(i)
                elif i == b[2]:
                    if stack[-1] == a[2]:
                        stack.pop()
                    else:
                        stack.append(i)
                else:
                    if stack[-1] == a[3]:
                        stack.pop()
                    else:
                        stack.append(i)
        else:               # 스택이 비어있으면 현재 문자 추가
            stack.append(i)

    if len(stack) == 0: # 스택이 비어있으면 완전한 문자열이므로 1반환, 불완전하다면 0반환
        return 1
    else:
        return 0