from collections import deque
r,c = map(int,input().split())
land = []
for i in range(r):
    land.append([0 for _ in range(c)])

k = int(input())
for i in range(k):
    b = list(map(int,input().split()))
    land[b[0]][b[1]] = 'x'

s = list(map(int,input().split()))
m = list(map(int,input().split()))
move = []
for i in m:
    if i == 1:
        move.append([-1,0])
    elif i == 2:
        move.append([1,0])
    elif i == 3:
        move.append([0,-1])
    else:
        move.append([0,1])

q = deque()
q.append(s)
z = 0

while q:
    x,y = q.popleft()
    land[x][y] = 'x'
    for _ in range(4):
        z1 = z%4
        nx = x + move[z1][0]
        ny = y + move[z1][1]

        if nx < 0 or ny < 0 or nx >= r or ny >= c:
            z += 1
            continue
        elif land[nx][ny] == 'x':
            z += 1
            continue
        elif land[nx][ny] == 0:
            q.append([nx,ny])
            break

print(x,y)