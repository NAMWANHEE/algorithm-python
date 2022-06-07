dx = [1,-1,0,0]
dy = [0,0,-1,1]
def dfs(x,y,cnt,result):
    result += li[x][y]
    if cnt == 6:
        ans.append(result)
        return
    for i in range(4):
        nx = dx[i] + x
        ny = dy[i] + y
        if 0<= nx < 4 and 0 <= ny < 4:
            dfs(nx,ny,cnt+1,result)
t = int(input())
for i in range(1,t+1):
    li = []
    for j in range(4):
        li.append(input().split())
    ans = []
    for x in range(4):
        for y in range(4):
            cnt = 0
            result = ''
            dfs(x,y,cnt,result)

    print('#'+str(i),len(set(ans)))