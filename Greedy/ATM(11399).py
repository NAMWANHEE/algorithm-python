n = int(input()) # 사람의 수
time = list(map(int,input().split())) # 각 사람이 돈을 인출하는데 걸리는 시간
time.sort() # 인출하는 시간이 적은 순으로 정렬
for i in range(1,n):
    time[i] = time[i-1] + time[i] # 각 사람이 돈을 인출하는데 걸리는 시간들의 합이 최소가 되도록 만드는 것이므로
                                  # 반복문을 통해 현재걸리는시간 = 현재걸리는시간 + 이전까지 걸린시간 으로 갱신
print(sum(time))