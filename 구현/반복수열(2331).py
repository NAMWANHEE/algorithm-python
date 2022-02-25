a,p = map(int,input().split()) # a: 수열의 첫번째 값, p: 이전 수열의 각 자리의 숫자를 곱하는 횟수
li = [a]    # 수열을 담는 리스트에 첫번째 값 설정
while True:
    num = 0 # 다음 수열의 값을 담을 변수
    for i in range(len(str(li[-1]))):
        num += int(str(li[-1])[i]) ** p # 리스트의 가장 마지막 값의 자릿수의 값에 p승 한 값을 더해줌

    if num in li:               # 구한 값이 이미 리스트에 있을 경우 ==> 반복 수열이 시작 되는 경우
        idx = li.index(num)     # 구한 값의 인덱스를 구하고 처음부터 반복수열이 시작되는 전까지의 길이 출력
        print(len(li[:idx]))
        break
    else:                       # 반복 수열이 나타나지 않으면 리스트에 값 추가가
       li.append(num)