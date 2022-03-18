from collections import deque


def solution(n, computers):
    answer = 0
    network = [0] * n  # 해당 컴퓨터에 방문했는지 체크하는 리스트

    def bfs(now): # 매개변수 now : 현재 컴퓨터 인덱스라고 생각하면 편할듯
        q = deque()
        q.append(now)
        network[now] = 1    # 현재 컴퓨터를 1로 방문 처리
        while q:
            s = q.popleft()
            for i in range(n):
                if computers[s][i] == 1 and network[i] == 0: # 현재 컴퓨터에 연결되어있고 방문처리가 안된 컴퓨터일 경우
                    q.append(i)    # 데크에 해당 컴퓨터 인덱스 추가
                    network[i] = 1 # 해당 컴퓨터 방문처리

    for i in range(n):
        if network[i] == 0: # 해당 컴퓨터 방문한적 없을때 bfs 실행 후 정답 카운트 +1
            bfs(i)
            answer += 1

    return answer