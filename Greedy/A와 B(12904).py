s = list(input())
t = list(input())

while True:
    if len(s) == len(t): # s와 t 의 길이가 같으면 반복문 종료
        break
    if t[-1] == 'A':     # t의 마지막 문자가 A일 경우 -> t 리스트 pop
        t.pop()
    else:
        t.pop()          # t의 마지막 문자가 B일 경우 -> t 리스트에서 pop을 한 후 문자열 뒤집기
        t = t[::-1]

if s == t:     # s 와 t 가 같다면 s를 t로 만들 수 있는 경우이므로 1출력
    print(1)
else:          # 만들 수 없는 경우 0출력
    print(0)