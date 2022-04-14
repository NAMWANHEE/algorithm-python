from itertools import permutations, combinations
n = int(input())
a = [i for i in range(1,n+1)]   # 1번 부터 n 번까지 선수담는 리스트
x = int(n/2)                    # 팀당 인원수 n/2
b = list(combinations(a,x))     # 선수들을 x인원으로 조합한 모든 경우
s = []                          # 각 선수들간의 능력치가 담길 이중리스트
for i in range(n):
    s.append(list(map(int,input().split())))    # 능력치 추가

answer = 100000
for i in range(len(b)//2):                 # 조합의 개수의 반까지만 반복
    team1 = b[i]                           # 팀이 가능한 조합
    team2 = b[-i-1]                        # 위의 조합에서 나머지 팀들의 조합
    sum1 = 0                               # team1 의 능력의 합을 담을 변수
    sum2 = 0                               # team2 의 능력의 합을 담을 변수
    for j in list(permutations(team1,2)):  # team1에서 2명씩 짝지은 모든 순열
        sum1 += s[j[0]-1][j[1]-1]          # 모든 순열에 대한 능력치의 합
    for j in list(permutations(team2,2)):  # 위와 동일한 방식으로 team2 의 능력치의 합을 구함
        sum2 += s[j[0]-1][j[1]-1]

    answer = min(answer,abs(sum1-sum2))    # team1 과 team2 의 능력치의 차이의 최소값을 반복을 통해 계속 갱신
print(answer)