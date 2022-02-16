import sys
import heapq
n = int(input())
time = [] # 전체 강의시간표
classroom = [] # 강의실의 끝나는 시간 담는 리스트 , 해당 리스트의 길이가 곧 강의실 갯수

for i in range(n):
    s, t = map(int,sys.stdin.readline().strip().split())
    time.append([s,t])

time.sort(key=lambda x: x[0]) # 강의 시작시간으로 정렬렬
heapq.heappush(classroom,time[0][1]) # 첫번째 강의 끝나는 시간을 우선순위 큐에 삽입

for i in range(1,n):                          # 두번째 강의실 부터 반복
    if time[i][0] < classroom[0]:             # 강의 시작시간이 강의 끝나는 시간보다 이르다면
        heapq.heappush(classroom, time[i][1]) # 강의실 하나 생성
    else:
        heapq.heappop(classroom)              # 강의시작시간이 끝나는 시간보다 같거나 늦으면
        heapq.heappush(classroom, time[i][1]) # 우선선위 큐에 가장 빨리끝나는 시간 삭제 후 현재 강의가 끝나는 시간 삽입
print(len(classroom))