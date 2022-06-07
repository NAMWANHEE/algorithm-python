from collections import deque
for _ in range(10):
    n = int(input())
    miro = []
    for i in range(16):
        miro.append(list(map(int,list(input()))))
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    q = deque()
    possible = False
    for i in range(16):
        break_point = False
        for j in range(16):
            if miro[i][j] == 2:
                q.append([i,j])
                miro[i][j] = 1
                break_point = True
        if break_point == True:
            break

    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y

            if nx < 0 or ny < 0 or nx >= 16 or ny >= 16:
                continue
            if miro[nx][ny] == 1:
                continue
            if miro[nx][ny] == 3:
                possible = True
                break
            miro[nx][ny] = 1
            q.append([nx,ny])

    if possible:
        print('#'+str(n),1)
    else:
        print('#'+str(n),0)