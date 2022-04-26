n = int(input())
in_car = {}
out_car = []
for i in range(n):  # 터널에 들어간 차량의 순서를 사전에 저장
    car = input()
    in_car[car] = i+1

for _ in range(n):  # 터널에서 빠져나온 차량의 순서대로 리스트에 저장
    car = input()
    out_car.append(car)
ans = 0

for i in range(n-1):
    for j in range(i+1,n):
        if in_car[out_car[i]] > in_car[out_car[j]]: # 현재 차량보다 늦게 터널에서 빠져나온 차량 중
            ans +=1                                 # 터널에 들어간 차량의 순서가 빠른경우
            break                                   # 정답 카운트 + 1 후 break
print(ans)