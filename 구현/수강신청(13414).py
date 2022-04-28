import sys
k, l = map(int,input().split())

stu = {}
for i in range(l):
    num = sys.stdin.readline().strip()  # 학번이 입력될때 마다 사전에서 value 값 갱신
    stu[num] = i+1                      # (중복 학번이 입력되면 자동으로 사전의 value 값이 현재 순번 으로 바뀜)

count = 0   # k명의 학생 카운트 하기위한 변수
for i in sorted(stu.items(),key=lambda x: x[1]):    # 사전의 value 값을 기준으로 정렬한 리스트
    if count == k:                                  # k 명이 될때까지 학번 출력
        break
    print(i[0])
    count += 1