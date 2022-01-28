n = int(input())                                # 게임구역의 크기
li =[]                                          # 게임판의 구역(맵)
for i in range(n):
    li.append(list(map(int,input().split())))
visit = [[False]*n for _ in range(n)]           # 방문한 구역 체크할 리스트

def dfs(a,b):                                   # 초기값 a,b 는 시작점인 0,0
    if a <= -1 or a >= n or b <= -1 or b >= n:  # 현재 위치가 게임판의 구역을 벗어나게 되면 조욜
        return False
    now = li[a][b]                              # 현재 위치의 값(이동할수있는값)
    if now == -1:                               # 현재 위치의 값이 -1(원하는 마지막 위치의 값)이면 HaruHaru 출력후 실행종료
        print('HaruHaru')
        exit(0)

    if visit[a][b] == False:                    # 만약 a,b 위치를 방문하지 않았다면
        visit[a][b] = True                      # 방문처리 한 후
        dfs(a+now,b)                            # 아래쪽로 now 만큼 이동한 값 재귀
        dfs(a,b+now)                            # 오른쪽로 now 만큼 이동한 값 재귀

dfs(0,0)
print('Hing')