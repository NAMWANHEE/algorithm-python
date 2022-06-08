from collections import deque
t = int(input())
for test in range(1,t+1):
    n = int(input())
    room = []
    for _ in range(n):
        room.append(list(map(int,input().split())))

    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    def bfs(xy):
        q = deque()
        q.append(xy)
        count = 0
        while q:
            x,y = q.popleft()
            for i in range(4):
                nx = dx[i] + x
                ny = dy[i] + y

                if nx < 0 or ny < 0 or nx >= n or ny >= n:
                    continue
                if room[nx][ny] == room[x][y] + 1:
                    q.append([nx,ny])
                    count += 1
        return count
    answer = {}
    for i in range(n):
        for j in range(n):
            answer[room[i][j]] = bfs([i,j])
    ans = sorted(answer.items(),key = lambda x : x[0],reverse=True)
    ans = sorted(ans,key = lambda x: x[1])
    print('#'+str(test),ans[-1][0],ans[-1][1]+1)