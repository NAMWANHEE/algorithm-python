n = int(input())
plus =[]    # 양수 담을 리스트
minus =[]   # 음수 담을 리스트
ans = 0     # 정답 담을 변수
zero = False # 0이 있는지 체크하는 변수

for i in range(n):
    a = int(input())
    if a == 1:          # 입력이 1일 경우
        ans += 1        # 1은 어떤 수와 곱해지지 않고 그냥 더하는게 최대값이 되기 때문에 그냥 정답에 1을 더해줌
    elif a > 1:         # 입력이 1보다 크다면
        plus.append(a)  # plus 리스트에 값 추가
    elif a == 0:        # 입력이 0이면
        zero = True     # 0있다고 체크
    elif a < 0:         # 입력이 음수인경우
        minus.append(a) # minus 리스트에 값 추가

plus.sort(reverse=True) # 양수는 내림차순으로
minus.sort()            # 음수는 오름차순으로 정렬

for i in range(0,len(plus),2):  # 양수인 경우 2개씩 정렬된 리스트에서 뽑아 곱한값을 정답에 추가해주고
    if i == len(plus)-1:        # 만약 양수가 담긴 리스트가 홀수일 경우는 마지막값을 정답에 더해줌
        ans += plus[i]
    else:
        ans += plus[i]*plus[i+1]

for i in range(0,len(minus),2): # 음수인 경우도 마찬가지고 2개씩 정렬된 리스트에서 뽑아 곱한값을 정답에 추가
    if i == len(minus)-1:       # 홀수인 경우에 0이 있으면 마지막 값과 곱하게 되어 0이 되므로 pass
        if zero:                # 0이 없는 경우엔 마지막값도 정답에 포함 시켜야하므로 정답에 마지막 값을 더해줌
            pass
        else:
            ans += minus[i]
    else:
        ans += minus[i]*minus[i+1]

print(ans)