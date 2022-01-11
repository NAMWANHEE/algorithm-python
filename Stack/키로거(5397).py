from collections import deque
import sys
n = int(input())
for i in range(n):
    a = sys.stdin.readline().strip()
    stack = deque()  # 2개의 deque를 이용하여 화살표가 나올때 마다 적절하게 옮겨줌
    li = deque()

    for i in a:
        if i == '<':    # < 화살표가 나올시 stack에 값(알파벳)이 있을시
            if stack :  # stack 에서 pop을한 값을 li 에 왼쪽에 추가
                li.appendleft(stack.pop())
        elif i == '>':  # > 화살표가 나올시 li에 값(알파벳) 이 있을시
            if li:      # li 왼쪽에서 pop을 한 값을 stack 에 추가
                stack.append(li.popleft())
        elif i =='-':   # - 백스페이스가 나올시 stack에서 pop
            if stack:
                stack.pop()
        else:           # 위에를 제외한 알파벳, 숫자등이 나올시 stack에 추가
            stack.append(i)
    print(''.join(list(stack)+list(li)))