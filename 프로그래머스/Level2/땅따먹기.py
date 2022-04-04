def solution(land):
    answer = 0

    for i in range(1, len(land)):       # 두번째 행부터 반복
        for j in range(len(land[0])):   # 4개의 열 반복
            a = 0
            for k in range(len(land[0])):
                if j == k:                  # 현재 열과 이전 열의 위치가 같으면 continue
                    continue
                a = max(a, land[i - 1][k])  # 이전 행에서 현재 열을 제외한 나머지 3개의 열중 가장 큰 값 a에 갱신하여 저장
            land[i][j] += a                 # 현재 위치의 값 = 현재 위치의 값 + 이전 행의 최대값 (DP)

    answer = max(land[-1])                  # 가장 마지막 행의 최대값이 정답
    return answer