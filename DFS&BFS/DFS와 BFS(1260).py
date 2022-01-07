n,m,v = map(int,input().split()) # n-노드수, m-간선수, v-시작노드
li = [[0]*(n+1) for _ in range(n+1)] # (n+1)x(n+1) 2차원 리스트 생성(인덱스 0이 들어가는 것은 무시 -> 실제로 사용하는 2차원리스트는 nxn
for i in range(m):
    a,b = map(int,input().split())
    li[a][b] = li[b][a] = 1 # 양방향이기 때문에 연결된 부분 양쪽 모두 1로 설정

visit = [0] * (n+1) # 인덱스 = 이미 방문한 노드라면 1, 방문하지 않은 노드는 0 (초기엔 0으로 설정)

def dfs(v):          # DFS - 깊이 우선 탐색
    visit[v] = 1     # v번 노드를 방문 -> 0을 1로변경
    print(v,end=' ') # 현재 노드 출력
    for i in range(1,n+1):
        if visit[i] == 0 and li[v][i] == 1: # 반복문을 돌며 아직 방문하지 않았고 연결되어있는 노드 탐색
            dfs(i)                          # dfs 함수 재귀

def bfs(v):
    visit2 = [v]        # visit2 는 방문해야 할 리스트
    visit[v]= 0         # dfs와 다르게 0이 방문한 것으로 여김

    while visit2:           # 방문해야할 곳이 남아있다면 계속 반복
        a = visit2.pop(0)   # 방문해야 할 곳 pop
        print(a,end=' ')    # pop 한 결과 출력
        for i in range(1,n+1):
            if visit[i] == 1 and li[a][i]: # 아직 방문하지 않았고 연결되어있다면
                visit2.append(i)           # 연결된 모든 노드를 방문해야할 리스트에 저장
                visit[i] = 0               # 연결된 노드 방문 처리
                                           # 위에서 pop(0)를 하여 스택이 아닌 먼저 들어간 값이 먼저나오는
                                           # FIFO 구조인 큐를 사용하여 BFS 구현
dfs(v)
print()
bfs(v)