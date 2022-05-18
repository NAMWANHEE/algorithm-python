n,m = map(int,input().split())
miro = []
for i in range(n):
    miro.append(list(map(int,input().split())))

for i in range(n):
    for j in range(m):
        if i-1 >= 0 and j-1 >= 0:
            miro[i][j] = miro[i][j] + max(miro[i-1][j],miro[i][j-1],miro[i-1][j-1])
        elif i-1 >= 0:
            miro[i][j] = miro[i][j] +miro[i-1][j]
        elif j-1 >= 0:
            miro[i][j] = miro[i][j] +miro[i][j-1]

print(miro[-1][-1])