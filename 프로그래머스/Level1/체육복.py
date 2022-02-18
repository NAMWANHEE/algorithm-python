def solution(n, lost, reserve):
    answer = 0
    c = 0   # 잃어버린 학생중 여분옷 받은 학생의 수
    lost.sort()
    for i in lost[:]:         # 잃어버린 학생중 여분의 옷을 가져온 학생이 있으면
        if i in reserve:      # 두 리스트에서 해당 학생 삭제
            reserve.remove(i)
            lost.remove(i)

    for i in lost:                # 잃어버린 학생 반복
        if i - 1 in reserve:      # 잃어버린 학생의 앞 번호 학생이 여분의 옷을 가져온경우
            reserve.remove(i - 1) # 여분옷 가져온 리스트에서 해당학생 삭제
            c += 1                # 카운트 +1
        elif i + 1 in reserve:    # 잃어버린 학생 다음학생이 여분의 옷을 가져온경우
            reserve.remove(i + 1) # 위와 동일
            c += 1
    answer = n - len(lost) + c    # 체육복 있는 학생 수 = 전체 - 안가져온 학생수 + 여분옷 받은 학생의 수
    return answer