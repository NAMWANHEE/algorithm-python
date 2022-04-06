def solution(N, stages):
    answer = []
    ans = []
    stages = sorted(stages)
    for i in range(1, N + 1):  # 1번 스테이지 부터 N번 스테이지까지
        a = len(stages)  # 현재 스테이지의 개수
        count = 0  # 스테이지에 도달했으나 클리어하지 못한 플레이어의 수를 담을 변수
        if a == 0:  # 스테이지에 도달한 유저가 없는 경우 [현재스테이지, 실패율(0)] 추가
            answer.append([i, 0])
        else:
            for j in stages:
                if i >= j:  # 현재 스테이지 보다 사용자가 도전하는 스테이지가 작거나 같을 경우
                    count += 1  # 클리어하지 못한 플레이어 수 카운트
                elif i < j:  # 스테이지가 정렬되어있으므로 사용자가 도전하는 스테이지가 클경우 break
                    break

            for s in range(count):  # 카운트 수만큼 스테이지 pop
                stages.pop(0)
            answer.append([i, count / a])  # [현재 스테이지, 실패율] 추가
    answer.sort(key=lambda x: x[1], reverse=True)  # 실패율의 내림차순으로 정렬
    for i in answer:
        ans.append(i[0])  # 위에 정렬한 리스트에서 스테이지만 리턴
    return ans