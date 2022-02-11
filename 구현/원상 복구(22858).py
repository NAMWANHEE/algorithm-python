n, k = map(int,input().split())
s = list(map(int,input().split())) # 수가 적혀있는 n개의 카드
d = list(map(int,input().split())) # d[i] 는 p[d[i]] 값을 i번째로 가지고오는것을 의미

for i in range(k):         # k번 섞었기 때문에 k번 반복하여 원래 카드 정보 추출
    ans = [0] * n          # 섞기 이전의 카드 정보를 담을 리스트
    for j in range(n):     # 카드 개수(n) 만큼 반복
        ans[d[j]-1] = s[j]  # 한번 섞기 이전의 카드 정보로 바꾸는 식
    s = ans                 # s를 섞기 이전의 카드 정보로 초기화

print(*ans)