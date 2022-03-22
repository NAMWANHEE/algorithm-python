from collections import deque
def solution(maps):
    answer = 0
    len_x = len(maps)       # maps 의 크기인 n x m 에서 최대 n 값
    len_y = len(maps[0])    # 최대 m 값
    dx = [-1, 1, 0, 0]      # 상 하 좌 우
    dy = [0, 0, 1, -1]
    start = [0, 0]          # 시작 지점
    q = deque()             # bfs 위한 큐(데크)생성
    q.append(start)         # 시작 지점 삽입

    while q:
        x, y = q.popleft()  # 좌표 추출
        if x == len_x - 1 and y == len_y - 1:   # 맵에 가장 마지막 위치일 경우 종료
            break
        plus = maps[x][y]   # 현재 맵(위치)의 값
        maps[x][y] = 0      # 현재 값을 0으로 변경

        for i in range(4):  # 상 하 좌 우 탐색
            nx = dx[i] + x
            ny = dy[i] + y

            if nx < 0 or ny < 0 or nx >= len_x or ny >= len_y:  # 게임 맵에서 좌표가 벗어날 경우 continue
                continue
            if maps[nx][ny] == 1:       # 이동하는 위치의 값이 1일때
                maps[nx][ny] = plus + 1 # 현재 값 + 1
                q.append([nx, ny])      # 큐에 이동 위치좌표 추가

    if maps[len_x - 1][len_y - 1] == 1: # 마지막 값이 1인 경우 (상대 진영 도달 x)
        answer = -1                     # -1 출력력
    else:
       answer = maps[len_x - 1][len_y - 1]
    return answer