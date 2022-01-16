import sys
from collections import deque
testcase = int(input())
for i in range(testcase):
    n,m = map(int,sys.stdin.readline().strip().split())
    c = list(map(int,sys.stdin.readline().strip().split()))
    li = deque()
    idx = 0
    for i in c:
        li.append([i,idx]) # deque 에 i: 문서의 중요도 idx: 해당 현재 인덱스
        idx+=1

    idx1 = 0
    ans = []
    while True:
        if idx1 == n:
            break
        s = True
        for i in range(1,len(li)):      # 리스트의 맨앞의 중요도보다 더큰 중요도가 뒤에 있다면
            if li[0][0] < li[i][0] :    # 리스트의 가장 뒤로 이동
                li.append(li.popleft()) # s = True 라면 맨앞의 중요도가 최대값임
                s = False               # s 변수를 통해 만약 맨앞에 있는 중요도가 최대값일때
                break                   # 기존 리스트에서 맨앞의 수(중요도가 최대인 값)를 ans(정답) 리스트에 추가
        if s == True:                   # ans의 갯수가 n과 같으면 반복문 종료
            idx1 += 1
            ans.append(li.popleft())
    cc = 0
    for j in ans:                       # ans 리스트를 돌며 원하는 인덱스(b)와 일치하는 순번 출력
        if j[1] == m:
            print(cc+1)
        else:
            cc += 1