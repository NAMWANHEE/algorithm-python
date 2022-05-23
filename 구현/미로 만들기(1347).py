li = [[0,0]]
n = int(input())
cmd = input()
move = [[1,0],[0,1],[-1,0],[0,-1]]
idx = 0
for i in cmd:

    if i == 'R':
        idx -= 1
    elif i == 'L':
        idx += 1
    elif i == 'F':
        a = move[idx%4]
        x,y = li[-1][0] + a[0], li[-1][1]+a[1]
        li.append([x,y])

x_rang = abs(min([i[0] for i in li]))+abs(max([i[0] for i in li]))
y_rang = abs(min([i[1] for i in li]))+abs(max([i[1] for i in li]))
x_n = 0
y_n = 0

if min([i[0] for i in li]) < 0:
    x_n = abs(min([i[0] for i in li]))
if min([i[1] for i in li]) < 0:
    y_n = abs(min([i[1] for i in li]))


ans = []
for i in range(x_rang+1):
    ans.append(['#']* (y_rang+1))

for x1,y1 in li:
    ans[x_n+x1][y_n+y1] = '.'

for i in ans:
    print(''.join(i))