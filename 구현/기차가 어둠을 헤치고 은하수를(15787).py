from collections import deque

n,m = map(int,input().split())              # n: 기차 수, m: 명령 수
train = [deque([0])*20 for _ in range(n)]   # 기차담을 리스트 , 기차의 칸은 20칸이므로 길이 20개짜리 데크를 n번 반복하여 생성
ans = [] # 정답 기차 담을 리스트

for r in range(m):
    command = list(map(int,input().split())) # 명령 (1,2일땐 3개 , 3,4일땐 2개라 리스트에 담아 이용)
    if command[0] == 1:                             # 명령 번호가 1일때
        if train[command[1]-1][command[2]-1] == 0:  # i번째 기차에 x번재 좌석에 사람이 없다면 태운다
            train[command[1]-1][command[2]-1] = 1
    elif command[0] == 2:                           # 명령 번호 2
        if train[command[1]-1][command[2]-1] == 1:  # i번재 기차에 x번째 좌석에 사람이 타있다면 하차시킨다
            train[command[1]-1][command[2]-1] = 0
    elif command[0] == 3:                           # 명령 번호 3
        train[command[1]-1].appendleft(0)           # 기차에 있는 승객들을 모두 한칸씩 뒤로 미룬다
        train[command[1] - 1].pop()                 # 데크를 이용하여 왼쪽에 0(빈좌석) 추가 후 pop

    elif command[0] == 4:                           # 명령 번호 4
        train[command[1] - 1].append(0)             # 기차에 있는 승객들을 모두 한칸씩 앞으로 땡긴다
        train[command[1] - 1].popleft()             # 빈 좌석(0)을 오른쪽에 추가시킨 후 가장 앞에 있는 값 pop


for i in train:
    flag = False            # 동일한 상태의 기차가 있는지 체크하기 위함
    if ans:                 # 은하수를 건널 수 있는 기차가 있는 경우
        for j in ans:       # 은하수를 건널 수 있는 기차와 현재 기차의 상태를 비교하여
            if j == i:      # 상태가 같지 않을 경우 추가(append)
                flag = True
                break
        if flag == False:
            ans.append(i)

    else:                   # 첫 기차는 무조건 은하수를 건널수 있으므로 추가
        ans.append(i)

print(len(ans))             # 은하수를 건널 수 있는 기차의 갯수 출력력