n, k = map(int, input().split())
num = input()
count = 0  # 숫자를 지운 횟수 카운트할 변수
stack = []  # 정답담을 스택
for i in num:  # 각 자리수만큼 반복
    if count == k:  # 숫자를 k개 지웠다면
        stack.append(i)  # 스택에 현재 숫자를 넣고 continue
        continue

    if not stack:  # 스택이 비어있을경우(초기상태)
        stack.append(i)  # 숫자를 스택에 추가
    else:
        for j in range(len(stack)):  # 현재 스택에 들어있는 숫자만큼 반복
            if stack[-1] < i:  # 스택의 마지막 값이 현재 숫자보다 작을 경우
                stack.pop()  # 스택의 마지막 값 pop
                count += 1  # 삭제 했으니 카운트 + 1

            else:  # 스택의 마지막값이 현재가 숫자보다 크거나 같을경우 현재 반복문 break
                break
            if count == k:  # 삭제한 횟수가 k와 같다면 break
                break
        stack.append(i)  # 스택에 현재 숫자 추가

while len(stack) != (n - k):  # 현재 스택의 길이가 (n-k) 와 같을때까지 반복하며 스택 pop
    stack.pop()
print(''.join(stack))