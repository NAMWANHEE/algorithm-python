n, m = map(int,input().split())
member = list(map(int,input().split()))

cost = []   # 각각 다음 원생간의 키차이를 담을 리스트
for i in range(len(member)-1):
    cost.append(member[i+1]-member[i]) # 자기 다음 사람과의 키차이를 추가
cost.sort() # 키 차이 별로 정렬

for i in range(m-1): # m-1 번 만큼 반복
    cost.pop()       # 키 차이가 큰 순으로 m-1 번 pop
print(sum(cost)) # 리스트의 총합이 티셔츠를 만드는 최소 비용