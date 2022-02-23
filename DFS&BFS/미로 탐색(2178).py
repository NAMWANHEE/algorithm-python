from collections import deque
n,m = map(int,input().split())
miro =[]        # 미로 n*m 배열
for i in range(n):
    miro.append(list(map(int,input())))

dx = [1,-1,0,0] # 상,하,좌,우
dy = [0,0,1,-1]

q = deque()     # 현재 위치 담을 데크
q.append([0,0]) # 맨 처음 위치인 0,0 대입

while q:              # bfs
    x,y = q.popleft() #

    for i in range(4):  # 상 하 좌 우 -> 4번 반복
        nx = x + dx[i]
        ny = y + dy[i]

        if nx < 0 or nx >= n or ny < 0 or ny >= m: # x,y 위치가 기존 미로범위보다 작거나 커지면 continue
            continue
        if miro[nx][ny] == 0:   # 미로의 위치의 값이 0이면 벽이므로 continue
            continue

        if miro[nx][ny] == 1:             # 이동하는 미로의 위치 값이 1인경우 (아직 방문 하지 않았다는 뜼)
            miro[nx][ny] = miro[x][y] + 1 # 이동하는 미로의 위치 값 = 현재 위치의 값 + 1
            q.append([nx,ny])             # 데크에 이동하는 위치의 x,y 값 추가

print(miro[n-1][m-1])