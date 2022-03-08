import copy
from collections import deque

w, l = map(int,input().split())
island = []
for i in range(w):
    island.append(list(input()))
dx = [1,-1,0,0]         # 상,하,좌,우
dy = [0,0,1,-1]

def bfs(a,b,land):
    land[a][b] = 0          # 첫 루트위치의 값을 0으로 초기화
    q = deque()             # 좌표 위치를 담을 데크
    q.append([a,b])         # 첫 루트위치의 좌표 데크에 추가
    c = 0                   # 현재 루트위치에서 최대 멀리떨어진 육지의 위치까지의 거리 값 담을 변수
    while q:
        x,y = q.popleft()   # 현재 좌표 위치 x,y

        for i in range(4):
            nx = dx[i] + x      # 이동한 위치의 x,y 좌표
            ny = dy[i] + y
            if nx < 0 or ny < 0 or nx >= w or ny >= l:  # 이동한 위치가 섬의 크기에 벗어나면 continue
                continue
            if land[nx][ny] == 'L':             # 이동한 위치의 값이 L = 육지 일때
                land[nx][ny] = land[x][y] + 1   # 해당 위치의 값을 현재 위치의 값 +1 을 해준다 (= 해당 육지 까지의 거리값)
                q.append([nx,ny])               # 데크에 이동한 위치 좌표 추가
                c  = max(c,land[nx][ny])        # 거리의 최대값 계속 갱신
    return c    # 현재 루트위치에서 최대 거리 값 반환
ans = []

for i in range(w):
    for j in range(l):
        if island[i][j] == 'L':         # 섬을 돌며 육지(L)이 나왔을때
            b = copy.deepcopy(island)   # 맨 처음 형태의 섬 복사
            ans.append(bfs(i,j,b))      # 현재 루트위치에서 최대 거리 값 ans 리스트에 추가

print(max(ans)) # 가장 큰 수 = 최대 거리