from collections import deque
def solution(progresses, speeds):  # progresses: 작업 진도가 담긴 리스트, speeds: 작업 속도가 담긴 리스트
    answer = []
    progresses = deque(progresses)
    speeds = deque(speeds)
    cnt = 0
    while progresses:
        cnt = 0
        if (100 -progresses[0]) % speeds[0] == 0:           # 만약 작업 진도가 작업 속도로 딱 나누어떨어지면
            a = int((100 -progresses[0]) / speeds[0])       # a 는 나눈 몫
        else:
            a = int((100 -progresses[0]) / speeds[0]) + 1   # 안나누어떨어지면 a는 나눈 몫에 +1
        for j in range(len(speeds)):
                progresses[j] += speeds[j] * a              # 반복문을 돌며 작업 진도에 작업속도*a 값을 더한값으로 갱신
        for i in range(len(speeds)):
            if progresses[0] >= 100:                        # 만약 작업진도가 100 이상이라면
                progresses.popleft()                        # 작업진도와 속도 모두 popleft()
                speeds.popleft()                            # cnt : 작업진도가 몇번이나 연속적으로 100이상인지 카운트
                cnt += 1
        if cnt !=0:                                         # cnt 가 0이 아니면 cnt 를 정답에 추가
            answer.append(cnt)
    return answer