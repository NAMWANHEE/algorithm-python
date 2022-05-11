from collections import deque
r,c = map(int,input().split())
land = []
for i in range(r):
    land.append(list(input()))
nx = [1,-1,0,0]
ny = [0,0,1,-1]
ans_dic = {'wolf':0,'sheep':0}

def bfs(a,dic):

    q = deque()
    q.append(a)
    land[a[0]][a[1]] = '#'
    while q:
        x,y = q.popleft()
        for i in range(4):
            dx = nx[i] + x
            dy = ny[i] + y
            if dx < 0 or dy < 0 or dx >= r or dy >= c:
                continue

            if land[dx][dy] == '#':
                continue
            elif land[dx][dy] == '.':
                q.append([dx,dy])
                land[dx][dy] = '#'
            elif land[dx][dy] == 'o':
                dic['sheep'] += 1
                q.append([dx,dy])
                land[dx][dy] = '#'
            elif land[dx][dy] == 'v':
                dic['wolf'] += 1
                q.append([dx,dy])
                land[dx][dy] = '#'

    if dic['wolf'] >= dic['sheep']:
        ans_dic['wolf'] += dic['wolf']
    else:
        ans_dic['sheep'] += dic['sheep']

for i in range(r):
    for j in range(c):
        dic = {'wolf': 0, 'sheep':0}
        if land[i][j] == 'v':
            dic['wolf'] += 1
            bfs([i,j],dic)

        elif land[i][j] == 'o':
            dic['sheep'] += 1
            bfs([i,j],dic)



print(ans_dic['sheep'],ans_dic['wolf'])