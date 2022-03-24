from collections import defaultdict


def solution(fees, records):
    incar = defaultdict(int)    # 입차 기록 담는 딕셔너리
    timedict = defaultdict(int) # 각 차량별 주차시간
    answer = []
    fulltime = 23 * 60 + 59     # 입차하고 출차는 하지 않을 경우 23:59 분에서 빼줘야 하므로 23:59분
    for i in records:
        number = i.split(' ')[1]            # 차량 번호
        time = i.split(' ')[0].split(':')   # 입차 or 출차 시간
        minute = int(time[0]) * 60 + int(time[1])   # 입차/출차 시간을 분으로 표현

        if i.split(' ')[-1] == 'IN':                # 입차인 경우
            incar[number] = minute                  # 입차 기록 담는 사전에 시간 갱신
        else:                                            # 출차인 경우
            timedict[number] += (minute - incar[number]) # 각 차량별 주차시간을 출차시간 - 입차한 시간으로 갱신
            incar[number] = -1                           # 입차 기록 -1로 변경

    for i in incar:                                      # 입차기록 담긴 리스트 조회
        if incar[i] != -1:                               # 입치 기록이 -1 이 아닌 경우 = 입차는 했지만 출차 하지 않은 경우
            timedict[i] += fulltime - incar[i]           # 해당 차량 번호의 주차기록에 23:59-입차한 시간을 더하여 갱신
            incar[i] = -1                                # 해당 차량 입차 기록 -1 로 변경

    for i in sorted(timedict):
        if timedict[i] <= fees[0]:  # 해당 차량의 주차시간이 기본시간보다 작거나 같을 경우
            answer.append(fees[1])  # 기본요금만 추가
        else:
            if (timedict[i] - fees[0]) % fees[2] == 0:                           # 초과 시간이 단위시간으로 나누어떨어지면
                fee = fees[1] + int((timedict[i] - fees[0]) / fees[2]) * fees[3] # 주차요금 징수 공식에 따라 추가
            else:                                                                      # 초과 시간이 단위시간으로 나누어떨어지지 않으면
                fee = fees[1] + (int((timedict[i] - fees[0]) / fees[2]) + 1) * fees[3] # 올림하여 요금 징수해야하므로 초과시간/단위시간에 +1 해주어 공식 대입
            answer.append(fee)
    return answer