import heapq
n = int(input())
li = list(int(input()) for _ in range(n))
heapq.heapify(li) # 파이썬의 heap 모듈 이용
ans = 0
while len(li) != 1:
    a = heapq.heappop(li) # a = 현재heap에서 가장 작은 원소 pop
    b = heapq.heappop(li) # b = 현재heap에서 가장 작은 원소 pop
    sum = a+b             # sum = 기존 heap에서 가장작은 원소 2개의 합
    ans += sum            # ans를 반복문마다 갱신
    heapq.heappush(li,sum) # heap에 가장 작은 원소 2개의 합을 추가

print(ans)