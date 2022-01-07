a, b = map(int,input().split()) # a: 동전의 종류 개수 b: 원하는 가치의 합
n= [] # 각 동전의 가치 담을 리스트
for i in range(a):
    n.append(int(input()))
n.sort(reverse=True) # 동전의 가치를 높은것부터 정렬
cnt = 0 # b 가격을 만족하는데 필요한 최소 동전 개수
while True:
    if b == 0: # 원하는 가치가 0이되면 반복문 종료
        break
    for i in range(len(n)):
        if n[i] <= b:               # 동전이 원하는 가격(b) 보다 낮을때
            cnt += b//n[i]          # 동전 개수 += 원하는 가치 합/ 현재 동전의 가치
            b = b-(n[i]*(b//n[i]))  # 현재 동전의 가치를 나눌 수 있는 가장 큰 동전으로 나눈 나머지
            n = n[i+1:]             # 현재 선택한 동전 보다 작은 값들만 나오도록 리스트 설정
            break
print(cnt)