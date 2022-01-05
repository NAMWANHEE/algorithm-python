e,s,m = map(int,input().split()) # e=지구, s=태양, m=달
a,b,c = 0,0,0 # a=e, b=s, c=m 으로 대응
cnt = 0 # 년도 카운트
while True:     # a,b,c 모두 1씩 증가하는 동시에 cnt 증가하면서
    cnt += 1    # 각각 a는 16, b는 29, c는 20이 될때마다 1로 초기화
    a += 1
    if a == 16:
        a = 1
    b += 1
    if b == 29:
        b = 1
    c += 1
    if c == 20:
        c = 1

    if a == e and b == s and c ==m: # a,b,c가 e,s,m과 똑같으면 반복문 종료
        break
print(cnt)