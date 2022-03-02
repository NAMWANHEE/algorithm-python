n = int(input())
home = []
for i in range(n):
    home.append(list(map(int,input().split())))

for i in range(1,n):                                                # 2번째 집부터 이전의 R,G,B 중 현재 색과 다른 두개 중 작은 비용과 현재 비용을 더한값을 현재 값으로 설정
    home[i][0] = min(home[i-1][1],home[i-1][2])+home[i][0]          # 현재 색상 R
    home[i][1] = min(home[i - 1][0], home[i - 1][2]) + home[i][1]   # 현재 색상 G
    home[i][2] = min(home[i - 1][1], home[i - 1][0]) + home[i][2]   # 현재 색상 B

print(min(home[n-1]))