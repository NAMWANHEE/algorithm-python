from collections import deque
n = int(input())
home = []
for i in range(n):
    home.append(list(input()))
dx = [1,-1,0,0]
dy = [0,0,1,-1]
ans = []

def bfs(xy):
    q = deque()
    q.append(xy)
    count = 1
    home[xy[0]][xy[1]] = '0'
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = dx[i]+x
            ny = dy[i]+y
            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue
            if home[nx][ny] == '1':
                count += 1
                home[nx][ny] = '0'
                q.append([nx,ny])
    ans.append(count)

for i in range(n):
    for j in range(n):
        if home[i][j] == '1':
            bfs([i,j])
            print(home)
ans.sort()
print(len(ans))
for i in ans:
    print(i)