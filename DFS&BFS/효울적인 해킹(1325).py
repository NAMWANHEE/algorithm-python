from collections import deque
import sys

a,b = map(int,input().split())
rel = [[] for _ in range(a+1)]
for i in range(b):
    x,y = map(int,sys.stdin.readline().strip().split())
    rel[y].append(x)    # y를 해킹 -> x도 해킹할 수 있다. (반대의 경우는 불가능)
                        # 따라서 y번째 리스트에 y를 해킹하면 해킹할수있는 컴퓨터(x)를 추가
def bfs(start):
    visit = [0] * (a + 1)   # 방문한 노드 체크할 리스트 ( 초기값 0 )
    q = deque()
    q.append(start)
    visit[start] = 1
    cnt = 1                 # 해킹 할 수 있는 컴퓨터 세기위한 변수
    while q:
        node = q.popleft()
        for i in rel[node]:
            if visit[i] == 0:
                q.append(i)
                visit[i] = 1
                cnt += 1
    return cnt
ans = []
for i in range(1,a+1):
    ans.append(bfs(i))  # 1부터 a 까지 각각  몇개를 해킹할 수 있는지 ans 리스트에 저장

ma = max(ans)           # 최대 해킹 가능한 컴퓨터 수

for i in range(len(ans)):
    if ans[i] == ma:        # ans 리스트에서 최대 해킹 수 와 같은 컴퓨터의 번호 출력
        print(i+1, end=' ')