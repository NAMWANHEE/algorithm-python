h,w,x,y = map(int,input().split())
li = []
for i in range(h+x):
    li.append(list(map(int,input().split())))


for i in range(h):
    for j in range(w):
        li[i+x][j+y] = li[i+x][j+y] - li[i][j]

for i in range(len(li)-x):
    print(*li[i][:-1])