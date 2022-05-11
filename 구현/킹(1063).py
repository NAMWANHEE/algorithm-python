a,b,n = input().split()
a1,a2 = a[0],a[1]
b1,b2 = b[0],b[1]

king = [abs(int(a2)-8),ord(a1)-65]
stone = [abs(int(b2)-8),ord(b1)-65]

move = {'R':(0,1),'L':(0,-1),'B':(1,0),'T':(-1,0),'RT':(-1,1),'LT':(-1,-1),'RB':(1,1),'LB':(1,-1)}

for i in range(int(n)):
    c = input()
    x1,x2 = move[c]
    if king[0]+x1 >= 8 or king[0]+x1 < 0 or king[1]+x2 >= 8 or king[1]+x2 < 0:
        continue
    if king[0]+x1 == stone[0] and king[1]+x2 == stone[1]:
        if stone[0]+x1 >= 8 or stone[0]+x1 < 0 or stone[1]+x2 >= 8 or stone[1]+x2<0:
            continue
        king[0] = king[0]+x1
        king[1] = king[1]+x2
        stone[0] = stone[0]+x1
        stone[1] = stone[1]+x2
    else:
        king[0] = king[0] + x1
        king[1] = king[1] + x2

king[0],king[1] = chr(king[1]+65), str(8-king[0])
stone[0],stone[1] = chr(stone[1]+65), str(8-stone[0])
print(king[0]+king[1])
print(stone[0]+stone[1])