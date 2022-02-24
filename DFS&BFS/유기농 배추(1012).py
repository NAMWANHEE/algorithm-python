from collections import deque

t = int(input()) # 테스트케이스

for i in range(t):
    n,m,k = map(int,input().split())    # n: 가로, m: 세로, k: 배추 개수
    ground = [[0]*n for _ in range(m)]  # 배추가 심어진 밭

    for i in range(k):
        x,y = map(int,input().split())
        ground[y][x] = 1                # 배추가 심어진 위치 1로 설정

    dx = [-1,1,0,0] # 상,하,좌,우
    dy = [0,0,-1,1]

    def bfs(a,b):
        q = deque()
        q.append([a,b])
        ground[a][b] = 0
        while q:
            x,y = q.popleft()
            for i in range(4):
                nx = x + dx[i]  # 상,하,좌,우 이동한 x,y 좌표
                ny = y + dy[i]

                if nx < 0 or ny < 0 or nx >= m or ny >= n:  # 이동한 위치가 밭의 범위를 벗어나지 않도록
                    continue
                if ground[nx][ny] == 0:         # 이동한 위치의 값이 0이 면 continue
                    continue

                if ground[nx][ny] == 1:         # 이동한 위치의 값이 1일때
                    q.append([nx,ny])           # 데크에 좌표 추가
                    ground[nx][ny] = 0          # 이동한 위치의 값 0으로 변경

    c = 0   # 독립된 땅의 개수 카운트할 변수

    for i in range(m):  # 행
        for j in range(n): # 열
            if ground[i][j] == 1:   # 만약 현재 위치의 값이 1이면 bfs 실행 후 카운트 + 1
                bfs(i,j)
                c += 1
    print(c)