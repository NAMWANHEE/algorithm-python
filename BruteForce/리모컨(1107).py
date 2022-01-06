ch = int(input()) # 가고 싶은 채널
n = int(input()) # 고장난 버튼의 개수
if n == 0:
    a = []
else:
    a = list(map(int,input().split())) # 고장난 버튼이 몇번인지 담을 리스트


ans = abs(ch-100) # 원하는 채널 - 현재 채널(100)

for i in range(1000001): # 이동하려는 채널이 0~500000까지이므로 1000000까지 설정하여 +,- 모두 생각해줌
    b = True
    for j in str(i):
        if int(j) in a: # 해당 채널의 숫자에 고장난 숫자가 포함되면 b = False 로 바꾸고 반복문 종료
            b = False
            break

    if b == True:  # 해당 채널의 숫자가 고장난 숫자가 없을때 최소 횟수를 ans 에 저장
        ans = min(ans,len(str(i))+abs(ch-i))
print(ans)

