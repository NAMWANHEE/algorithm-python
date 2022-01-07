import sys
n,m, = map(int,input().split()) # n-노드수, m-간선수,
li = [[0]*(n+1) for _ in range(n+1)] # (n+1)x(n+1) 2차원 리스트 생성(인덱스 0이 들어가는 것은 무시 -> 실제로 사용하는 2차원리스트는 nxn
for i in range(m):
    a,b = map(int,sys.stdin.readline().strip().split())
    li[a][b] = li[b][a] = 1 # 양방향이기 때문에 연결된 부분 양쪽 모두 1로 설정

visit = [0] * (n+1) # 인덱스 = 이미 방문한 노드라면 1, 방문하지 않은 노드는 0 (초기엔 0으로 설정)
def bfs(v):
    visit[v]= 1
    visit2 =[v]
    while visit2:
        a = visit2.pop(0)
        for i in range(1,n+1):
            if visit[i] == 0 and li[a][i]:
                visit2.append(i)
                visit[i] = 1
answer = 0
for i in range(1,n+1):
    if visit[i] == 0:   # bfs 를 이용하여 먼저 1부터 시작하여 1과 연결된 모든 노드를 찾고
        bfs(i)          # 방문 리스트에 방문한 노드를 1로 바꿔줌
        answer += 1     # bfs 함수가 모두 돌면 연결 요소(answer += 1)
print(answer)           # 반복문을 돌며 방문안한 노드가 있으면 bfs 함수 실행
