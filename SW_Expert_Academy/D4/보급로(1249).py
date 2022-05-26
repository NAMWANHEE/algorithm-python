from collections import deque
t = int(input())
for test in range(1,t+1):
    n = int(input())
    road = []
    answer = [[1000000]*n for _ in range(n)]
    answer[0][0] = 0
    for i in range(n):
        road.append(list(map(int,list(input()))))
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    q = deque()
    q.append([0,0])

    while q:
        x,y = q.popleft()

        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y

            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue
            if answer[nx][ny] > road[nx][ny] + answer[x][y]:
                answer[nx][ny] = road[nx][ny] + answer[x][y]
                q.append([nx,ny])

    print('#'+str(test),answer[-1][-1])