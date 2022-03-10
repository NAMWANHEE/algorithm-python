from collections import deque
import copy

def solution(places):
    answer = []
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    def bfs(place):
        b = deque()
        a = True
        place2 = []
        for i in place:
            place2.append(list(i))
        for j in range(5):
            for s in range(5):
                if place2[j][s] == 'P':     # 응시자가 있는 좌표만 추가
                    b.append([j, s])

        if len(b) == 0: # 응시자가 0명일 경우 1 리턴
            return 1

        for i in b:                         # 응시자 좌표 반복
            queue = deque()                 # 큐 생성
            queue.append(i)                 # 큐에 응시자 좌표 추가
            place3 = copy.deepcopy(place2)  # 현재 대기실 복사
            place3[i[0]][i[1]] = 0          # 대기실의 현재 응시자 좌표에 해당값 0으로 초기화
            while queue:
                x, y = queue.popleft()      # x,y 좌표 pop

                for i in range(4):
                    nx = dx[i] + x
                    ny = dy[i] + y
                    if nx < 0 or ny < 0 or nx >= 5 or ny >= 5:  # 이동한 좌표가 대기실 범위 밖이면 continue
                        continue
                    if place3[nx][ny] == 'X':   # 이동한 위치가 X(벽)이면 continue
                        continue
                    if place3[nx][ny] == 'O':             # 이동한 위치가 O(테이블)이면
                        place3[nx][ny] = place3[x][y] + 1 # 이전 위치의 값 + 1
                        queue.append([nx,ny])             # 큐에 이동한 위치 좌표 추가
                    elif place3[nx][ny] == 'P':           # 이동한 위치가 P(다른 응시자) 라면
                        if place3[x][y]+1 <= 2:           # 이동하기전 값 +1 이 2보다 작다면(= 맨해튼 거리가 2 이하) 0 반환
                            return 0
                        queue.append([nx,ny])             # 거리가 2초과일 경우 큐에 좌표 추가
                        place3[nx][ny] = 0                # 이동한 위치의 값 0으로 초기화
        return 1    # 모두 거리두기에 성공한 경우 1반환

    for i in places:
        answer.append(bfs(i))

    return answer