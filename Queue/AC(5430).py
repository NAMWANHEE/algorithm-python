import sys
from collections import deque
n = int(input())  # 테스트케이스 개수
for i in range(n):
    a = sys.stdin.readline().strip()  # 수행할 함수(R또는D)
    b = int(sys.stdin.readline().strip()) # 배열에 들어있는 수의 개수
    c = sys.stdin.readline().strip()  # [1,2,3,4] 와같은 형태의 배열을 입력
    if len(c) != 2:              # 입력받은 배열이 [] 괄호만 있는경우를 제외한 모든 경우
        c = c[1:-1].split(',')   # 괄호를 없애고 ','기준으로 나눔
        c = deque(c)
    else:                        # [] 괄호만 있는 경우
        c = deque()
    try:
        front = True             # front 가 True라면 popleft(): 첫번째 값 삭제
        for i in a:              # False라면 pop() : 마지막 값 삭제
            if i =='R':          # R 명령어가 나오면 front 값에 따라 반대로 변경
                if front == True:
                    front = False
                else:
                    front = True
            else:
                if front == True:
                    c.popleft()
                else:
                    c.pop()
        if front == False:         # front가 False라면 deque를 뒤집어준다.
            c.reverse()            # True인경우는 R이 안나오거나 R이 짝수번 나온경우로
        print('['+",".join(c)+']') # reverse할 필요가없다.
    except:
        print('error')