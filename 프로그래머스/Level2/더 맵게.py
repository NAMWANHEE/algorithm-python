import heapq
def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville) # 스코빌 리스트를 힙으로 만들어준 후
    while scoville[0] < K:  # 가장 약한 스코빌이 K보다 작다면 계속 반복
        heapq.heappush(scoville,heapq.heappop(scoville) + heapq.heappop(scoville)*2) # 스코빌 리스트에 (가장 약한 스코빌 + 그다음 약한 스코빌*2)의 값을 추가
        answer += 1 # 카운트 +1
        if scoville[0] < K and len(scoville) == 1: # 스코빌이 K 이상인 경우가 없을때 정답은 -1
            return -1
    return answer