n= int(input())
li = []
for i in range(n):
    li.append(list(map(int,input().split())))
m = max(x[1] for x in li)
li = sorted(li,key=lambda x:x[0])
new = []
m1 = 0
for i in range(len(li)):
    if li[i][1] == m:
        new.append(li[i])
        break
    else:
        if li[i][1] > m1:
            m1 = li[i][1]
            new.append(li[i])

m2 = 0
for i in range(-1,-len(li)-1,-1):

    if li[i][1] == m:
        new.append([li[i][0]+1,li[i][1]])
        break
    else:
        if li[i][1] > m2:
            m2 = li[i][1]
            new.append([li[i][0]+1,li[i][1]])

if new[-1] in new[:-1]:
    new = new[:-1]
new = sorted(new,key=lambda x:x[0])

ans = 0
for i in range(len(new)-1):
    if new[i][1] > new[i+1][1]:
        ans += new[i+1][1] * abs(new[i+1][0] - new[i][0])
    else:
        ans += new[i][1] * abs(new[i + 1][0] - new[i][0])

print(ans)