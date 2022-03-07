import sys
t = int(input())
for i in range(t):
    n = int(sys.stdin.readline())   # 지원자 수
    li = []   # 지원자의 서류 성적, 면접 성적 넣을 리스트
    c = 0     # 신입사원 인원수 담을 변수 (= 정답)

    for i in range(n):
        li.append(list(map(int,sys.stdin.readline().split())))
    li = sorted(li,key = lambda x: x[0])    # 지원자의 서류 성적이 좋은 순으로 정렬 (1이 가장 좋은 성적)
    now = i[0][1] # 현재 최고 면접성적( 초기값은 서류성적이 1등인사람의 면접성적)

    for i in li:
        if i[0]==1 or i[1]==1:  # 면접 점수 or 서류 점수가 1등이면
            c+=1                # 무조건 신입사원 추가
            continue

        if i[1] < now:      # 서류 성적은 안좋지만 면접성적이 좋은 경우 (= 현재 지원자의 면접 성적이 기존의 최대 면접성적보다 좋을 경우)
            c+=1            # 신입사원 추가
            now = i[1]      # now를 현재 지원자의 면접 성적으로 초기화
    print(c)