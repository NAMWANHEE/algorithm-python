import copy
from collections import deque

def bfs(l,i,j):             # bfs , l: 현재 지역의 높이가 담긴 리스트, i: x좌표, j: y좌표
    q = deque()             # 큐 생성
    q.append([i,j])         # 큐에 x,y 좌표 삽입
    l[i][j] = 0             # 해당 위치의 높이 0으로 변경
    while q:
        x,y = q.popleft()
        for i in range(4):  # 상 하 좌 우 탐색
            nx = x+dx[i]
            ny = y+dy[i]

            if nx < 0 or ny < 0 or nx > n-1 or ny > n-1:    # 지역의 범위를 벗어날 경우 continue
                continue
            if l[nx][ny] == 0:  # 이동 지역의 높이가 0인경우 continue
                continue
            else:               # 이동한 지역의 높이가 0이 아니고 정상적인 범위안에 있다면
                l[nx][ny] = 0   # 이동한 위치의 높이를 0으로 변경
                q.append([nx,ny])   # 큐에 이동한 x,y 좌표 추가

n = int(input())
land2 = []  # 각 지역의 높이 정보를 담을 2차원 리스트
max_num = 0 # 각 지역의 높이중 최대 높이를 담을 변수
answer_list =[] # 정답 담을 리스트

for i in range(n):
    a = list(map(int,input().split()))
    max_num = max(max_num,max(a))
    land2.append(a)
dx = [1,-1,0,0]
dy = [0,0,1,-1]

for i in range(1,max_num):      # 1부터 최대 높이전 까지 반복
    answer = 0
    land = copy.deepcopy(land2) # 매 반복마다 새로운 지역정보를 사용
    for j in range(n):
        for k in range(n):
            if land[j][k] <= i: # 각 지역을 돌며 i(강수량) 보다 작거나 같다면 (= 물에 잠기면)
                land[j][k] = 0  # 물에 잠긴 지역의 값을 0으로 변경
    for i in range(n):
        for j in range(n):
            if land[i][j] != 0: # 각 지역을 돌며 해당 지역이 0이 아닌경우
                bfs(land,i,j)   # bfs 실행
                answer += 1     # 정답 카운트 + 1
    answer_list.append(answer)  # 정답을 정답 리스트에 추가

if len(answer_list) == 0:   # 땅의 최대 높이가 1인경우, 모든 땅의 높이가 1인 경우
    print(1)                # 안전 영역은 1개뿐
else:
    print(max(answer_list)) # 정답들이 담긴 리스트중 최대값