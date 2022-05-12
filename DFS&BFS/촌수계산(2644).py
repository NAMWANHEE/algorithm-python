from collections import deque
n = int(input())
a,b = map(int,input().split())
m = int(input())
relation = {i:[] for i in range(1,n+1)}
visit = [0]* (n+1)

for i in range(m):
    x,y = map(int,input().split())
    relation[x].append(y)
    relation[y].append(x)
q = deque()
q.append(a)
visit[a] = 1
cnt = 0
def bfs(li):
    re = deque()
    while li:
        w = li.popleft()
        for i in relation[w]:
            if i == b:
                return 0
            if visit[i] == 0:
                visit[i] =1
                re.append(i)
    return re

while True:
    q = bfs(q)
    cnt += 1
    if q == 0:
        print(cnt)
        break
    if len(q) == 0:
        print(-1)
        break