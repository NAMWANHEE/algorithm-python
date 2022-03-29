def solution(n):
    answer = 1              # n 자기 자신도 카운트 이므로 정답에 1을 추가하고 시작
    li = [i for i in range(1,n+1)]  # 1~n까지 담은 리스트
    idx = 0                         # 시작 인덱스
    while idx <= int(n/2)-1:        # 연속된 값의 합이 n 이 되기 위해서 최대 시작값은 n/2의 정수값이다 따라서 인덱스는 -1을 해줘야하므로 idx가 해당값을 이하일때만 반복
        sum_num = 0                 # 연속값의 합을 담을 변수
        for i in range(idx,n-1):    # 위에서 구한 인덱스 값부터 n-1까지 반복
            sum_num += li[i]        # 연속값의 합을 계속 갱신
            if sum_num == n:        # 연속값의 합이 n일경우 정답 카운트 + 1, 현재 반복문 종료
                answer += 1
                break
            if sum_num > n:         # 연속값의 합이 n 초과일 경우, 현재 반복문 종료
                break
        idx += 1                    # 시작 인덱스 + 1
    return answer