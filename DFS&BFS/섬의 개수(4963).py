from collections import deque
dx = [1,-1,0,0,1,1,-1,-1]   # 상 하 좌 우 대각선 체크
dy = [0,0,1,-1,1,-1,1,-1]
while True:
    w,h = map(int,input().split())
    if w == 0 and h == 0:   # 0,0 입력시 종료
        break
    maps = []
    for i in range(h):
        maps.append(list(map(int,input().split())))
    visit = [[0]*w for _ in range(h)]   # 해당 섬 방문체크


    def bfs(i,j):
        q = deque()
        q.append([i,j])
        while q:
            x,y = q.popleft()
            for i in range(8):
                nx = dx[i] + x
                ny = dy[i] + y

                if nx < 0 or ny < 0 or nx > h-1 or ny > w-1 or visit[nx][ny] == 1: # 이동한 위치가 맵의 범위를 벗어나거나 방문한 곳일 경우 continue
                    continue
                if maps[nx][ny] == 0:   # 이동한 위치가 바다일 경우 continue
                    continue
                else:
                    visit[nx][ny] = 1   # 이동한 위치가 섬이고 방문한적이없다면 방문처리 후
                    q.append([nx,ny])   # 큐에 좌표 추가

    answer = 0
    for i in range(h):
        for j in range(w):
            if maps[i][j] == 1 and visit[i][j] == 0:    # 해당 위치가 섬이고 방문한적이 없다면
                visit[i][j] = 1                         # 방문 처리 후 bfs 실행
                bfs(i,j)                                # 정답 카운트 + 1
                answer += 1
    print(answer)