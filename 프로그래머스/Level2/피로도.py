from itertools import permutations

def solution(k, dungeons):  # k: 유저의 현재 피로도, dungeons: 각 던전의 "최소 필요 피로도","소모 피로도" 가 담긴 리스트
    answer = -1
    leng = len(dungeons)

    for i in permutations(dungeons, leng):  # 던전 리스트와 던전의 개수로 순열 생성
        count = 0   # 현재 순열의 탐험 횟수 담을 변수
        k2 = k      # 유저의 현재 피로도
        for j in i:
            if j[0] <= k2 and j[1] <= k2:   # 유저의 피로도 보다 현재 던전의 요구 피로도와 소모 피로도 둘다 적을때
                k2 = k2 - j[1]              # 유저의 피로도 = 유저의 피로도 - 소모 피로도
                count += 1                  # 카운트 + 1

        answer = max(answer, count)         # 현재 순열의 탐험 횟수와 이전의 탐험 횟수 중 큰 값으로 정답 갱신

    return answer