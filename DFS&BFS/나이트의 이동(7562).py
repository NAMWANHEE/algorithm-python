from collections import deque
dx = [-1,-2,1,2,-1,-2,1,2]
dy = [2,1,2,1,-2,-1,-2,-1]

n = int(input())
for i in range(n):
    x1 = int(input())
    maps = [[0]*x1 for _ in range(x1)]

    night = list(map(int,input().split()))
    a,b = map(int,input().split())
    if night[0] == a and night[1] == b:
        print(0)
        continue
    q = deque()
    q.append(night)

    flag = False
    while q:
        x,y = q.popleft()
        for i in range(8):
            nx = x+dx[i]
            ny = y+dy[i]

            if nx < 0 or ny < 0 or nx >= x1 or ny >= x1:
                continue
            if maps[nx][ny] != 0:
                continue
            maps[nx][ny] = maps[x][y] + 1
            if nx == a and ny == b:
                flag = True
                break
            q.append([nx,ny])
        if flag == True:
            break
    print(maps[a][b])