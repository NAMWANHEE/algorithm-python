def solution(triangle):
    answer = 0

    for i in range(1, len(triangle)):
        for j in range(len(triangle[i])):           # 삼각형의 두번째 줄 부터
            if j == 0:                              # 맨 왼쪽의 값들은 바로 전 단계의 가장 왼쪽값을 더해줌
                triangle[i][0] += triangle[i - 1][0]
            elif j == len(triangle[i]) - 1:         # 맨 오른쪽 값들은 바로 전 단계의 가장 오른쪽값을 더해줌
                triangle[i][j] += triangle[i - 1][j - 1]
            else:                                   # 나머지인 경우들은 바로 전 단계의 현재와 동일한 인덱스의 값과 이전 인덱스의 값 중 더 큰 값을 더해서 갱신
                triangle[i][j] += max(triangle[i - 1][j], triangle[i - 1][j - 1])
    answer = max(triangle[-1])                      # 삼각형의 마지막 줄에서 가장 큰 값이 정답
    return answer