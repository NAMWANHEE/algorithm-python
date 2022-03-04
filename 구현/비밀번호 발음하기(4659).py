vowel = ['a','e','i','o','u']
def check(str):
    ja = 0  # 자음이 3개이상인 경우 체크하기위한 변수
    mo = 0  # 모음이 3개이상인 경우 체크하기위한 변수
    mocheck = 0     # 입력한 패스워드에 모음이 있는지 체크하는 변수
    compare = '-'   # 이전에 나온 문자 저장, 연속적으로 2번나오는 문자가 있는지 체크하기 위한 변수

    for i in str:
        if i == compare and i != 'e' and i != 'o' : # 이전 문자와 동일하고, 두번 연속된 문자가 e 와 o 가 아닌 경우
            return 0                                # 0 반환
        else:                                       # 연속되지 않은 경우
            compare = i                             # 현재문자를 이전 문자저장하는 변수에 저장

        if mocheck:                  # 이미 해당 패스워드에 모음이 있는 경우
            if i in vowel:           # 현재 문자가 모음인 경우
                mo +=1               # 모음 카운트 +1
                ja = 0               # 이전에 자음이 카운트되었을 경우를 대비해 자음 카운트 0으로 초기화
            else:                    # 현재 문자가 자음인 경우 위와 동일한 방식으로 체크
                mo = 0
                ja += 1
            if mo == 3 or ja == 3:  # 모음또는 자음이 3개연속으로 나오는경우 0 반환
                return 0
        else:                       # 모음이 없는 경우
            if i in vowel:
                mocheck = 1         # 현재 문자가 모음인 경우 모음체크 1로 초기화
                mo += 1             # 나머지는 위와 동일
                ja = 0
            else:
                mo = 0
                ja += 1
            if mo == 3 or ja == 3:
                return 0

    if mocheck: # 모든 규칙 만족하는 경우 1반환
        return 1
    else:       # 모음이 하나도 없는 경우 0 반환
        return 0
while True:
    n = input()
    if n == 'end':  # end 입력시 종료
        break
    if check(n):                        # 1 = 규칙이 만족할 경우
        print("<"+n+"> is acceptable.")
    else:                               # 규칙이 만족하지 않을 경우
        print("<"+n+"> is not acceptable.")