n = int(input())
ball = list(map(int,input().split()))
ball_count = 0  # 타자당 볼의 갯수 카운트
base = [0,0,0]  # 3,2,1 루  , 0 : 주자x , 1: 주자o
point = []      # 점수

def points():                   # 주자가 1루로 나갈 경우 1,2,3 루의 상태에 따라 베이스 상태 변경하는 함수
    if base[-1] == 0:           # 주자가 1루에 없을땐 1루에 주자 투입
        base[-1] = 1
    elif base[-1] == 1:         # 주자가 1루에 있을때
        if base[1] == 0:        # 2루에는 없을경우
            base[1] = 1         # 2루에 주자 투입
        elif base[1] == 1:      # 2루에 주자가 있을 경우
            if base[0] == 0:    # 3루에 주자가 없으면
                base[0] = 1     # 3루에 주자 투입
            else:               # 3루에 주자가 있을경우
                base[0] = 1     # 3루에 주자 투입 후 점수 1추가
                point.append(1)

for i in ball:
    if i == 1:              # 볼이 나올 경우
        ball_count += 1     # 볼카운트 +1
        if ball_count == 4: # 볼이 4개가 된 경우
            points()        # points 함수 호출
            ball_count = 0  # 주자가 나갔으니 볼카운트 0으로 초기화

    elif i == 2:            # 데드볼인 경우
        ball_count = 0      # 주자는 무조건 진루하므로 볼카운트 0 초기화
        points()            # points 함수 호출

    elif i == 3:            # 폭투인 경우는 볼로 취급, 하지만 1,2루에 주자가 있을 경우 2,3루로 진루, 3루에 주자가 있을경우 홈으로 들어와 1득점
        ball_count += 1     # 볼카운트 +1
        base.append(0)      # base에 0을 추가하여 현재 타자는 진루하지 않을 상태로 만들고 나머지는 다 1개씩 진루
        point.append(base[0]) # 3루에 사람이 있다면 1점 추가, 사람이 없었다면 0점추가
        base = base[1:]       # 베이스를 1~3번인덱스로 초기화
        if ball_count == 4:   # 폭투도 볼로 취급하여 볼인경우와 동일
            points()
            ball_count = 0
try:                   # 점수가 안나면 빈 리스트인 경우가 있어 예외처리
    print(sum(point))
except:
    print(0)