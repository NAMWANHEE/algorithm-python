n = int(input())
k = int(input())
sensor = sorted(list(set(list(map(int,input().split())))))
if k >= n:  # 센서보다 집중국이 많을 경우
    print(0)
else:
    a = [] # 정렬된 각 센서값 사이의 거리를 담을 리스트
    for i in range(len(sensor)-1):
        a.append(sensor[i+1]-sensor[i]) # 바로 옆의 센서와의 거리 차이 추가
    a.sort()    # 거리를 오름차순으로 정렬

    for i in range(k-1): # k-1 번 만큼 가장 거리가 큰 값을 반복해서 pop
        a.pop()
    print(sum(a)) # 답: 남아있는 센서간의 거리들의 총합