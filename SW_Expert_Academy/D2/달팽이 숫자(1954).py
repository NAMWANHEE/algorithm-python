t = int(input())
for test in range(1,t+1):
    n = int(input())
    snail = [[0]*n for _ in range(n)]
    move = [[0,1],[1,0],[0,-1],[-1,0]]
    x,y = 0,0
    snail[0][0] = 1
    idx = 0
    while snail[x][y] != n**2:
        nx = x + move[idx][0]
        ny = y + move[idx][1]
        if nx < 0 or ny < 0 or nx >= n or ny >= n or snail[nx][ny] != 0:
            idx = (idx+1) % 4
        else:
            snail[nx][ny] = snail[x][y] + 1
            x = nx
            y = ny

    print('#' + str(test))
    for i in snail:
        print(*i)