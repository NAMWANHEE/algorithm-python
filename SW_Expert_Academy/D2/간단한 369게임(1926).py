n = int(input())
li = [str(i) for i in range(1,n+1)]
ban =['3','6','9']
answer = []
for i in li:
    count = 0
    for j in i:
        if j in ban:
            count += 1
    if count == 0:
        answer.append(i)
    else:
        answer.append('-'*count)
print(*answer)