import copy
from collections import deque

def bfs(xy, lad):
    q = deque()
    q.append(xy)
    lad[xy[0]][xy[1]] = 0
    flag = False
    while q:
        x, y = q.popleft()
        if lad[x][y] == 2:
            flag = True
            break
        lad[x][y] = 0
        for i in range(3):
            nx = dx[i] + x
            ny = dy[i] + y

            if nx < 0 or ny < 0 or nx >= 100 or ny >= 100:
                continue
            if lad[nx][ny] == 0:
                continue
            q.append([nx, ny])
            break
    if flag == True:
        return 1
    else:
        return 0
    
for _ in range(10):
    n = int(input())
    ladder = []
    dx = [0,0,1]
    dy = [1,-1,0]
    for _ in range(100):
        ladder.append(list(map(int,input().split())))

    for i in range(100):
        if ladder[0][i] == 1:
            s = copy.deepcopy(ladder)
            if bfs([0,i],s):
                print('#'+str(n),i)