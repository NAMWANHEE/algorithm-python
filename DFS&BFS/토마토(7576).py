import sys
from collections import deque
m,n = map(int,input().split())
tmt =[]
for i in range(n):
    tmt.append(list(map(int,input().split())))

queue = deque()
for i in range(n):
    for j in range(m):
        if tmt[i][j] == 1:
            queue.append([i,j]) # 맨 처음 익은 상태의 토마토만 데크에 추가

dx = [-1,1,0,0]
dy = [0,0,-1,1]

while queue:              # bfs
    x,y = queue.popleft() # 익은 토마토의 위치
    for i in range(4):    # 반복문 4번으로 상 하 좌 우 탐색
        nx = dx[i]+x      # 이동한 위치의 x좌표 = nx
        ny = dy[i]+y      # 이동한 위치의 y좌표 = ny
        if nx < 0 or ny < 0 or nx >n-1 or ny > m-1: # 이동한 x,y가 상자 크기의 범위를 벗어날 경우 continue
            continue

        if tmt[nx][ny] == 0:            # 이동한 위치의 토마토가 익지 않은 0이라면
            tmt[nx][ny] = tmt[x][y] + 1 # 현재 익은 토마토의 값에 +1 , 이렇게 하는 이유는 토마토가 익는 날짜를 알기 위해 +1을 해준다
            queue.append([nx,ny])       # 이동한 좌표값 데크에 추가

ans = 0
for i in range(n):
    for j in range(m):
        if tmt[i][j] == 0:     # 위의 과정을 다 돌았는데도 0이 있는 경우 = 토마토가 모두 익지 못하는 상황
            print(-1)          # -1 출력 후 종료
            sys.exit(0)
    ans = max(ans,max(tmt[i])) # n 개의 리스트를 반복하며 최대값 갱신

print(ans-1)                   # 가장 최대값에 -1을 해줘야 경과된 날짜가 된다.