from collections import deque
import copy

def solution(s):
    answer = -1
    ans = []        # 최종 문자열 담을 리스트
    s = deque(s)    # 문자열 -> 데크로 변환
    for i in copy.deepcopy(s): # i => 문자
        if len(ans) == 0:   # 정답 리스트가 비어있을땐 현재 문자 추가
            ans.append(i)   # 기존 리스트에서 현재문자 제거
            s.popleft()
            continue

        if ans[-1] == i:    # 연속된 두 문자일경우
            ans.pop()       # 둘다 제거
            s.popleft()
        else:               # 연속한 문자열이 아닐경우
            ans.append(i)   # ans 리스트에 문자 추가
            s.popleft()     # s 데크에서는 문자 삭제

    if ans:           # 최종 문자열이 있는 경우
        answer = 0
    else:             # 연속되는 문자열이 계속 삭제되어 문자열이 없는경우우
        anwer = 1

    return answer