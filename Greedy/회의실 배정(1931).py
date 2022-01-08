import sys
n = int(input())
li = []
for i in range(n):
    a, b = map(int,sys.stdin.readline().strip().split())
    li.append([a,b])

li = sorted(li, key=lambda a: a[0]) # 시작시간에 대해 정렬 후
li = sorted(li, key=lambda a: a[1]) # 끝나는 시간에 대해 정렬

finish = 0 # 끝나는 시간
cnt = 0    # 회의 개수 카운트
for i in li:
    if finish <= i[0]: # 회의 시작시간이 이전 회의가 끝나는 시간보다 늦을 경우
        finish = i[1]  # finish에 이제 할 회의의 끝나는 시간 저장
        cnt += 1       # 회의 카운트
print(cnt)