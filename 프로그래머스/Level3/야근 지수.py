import heapq
def solution(n, works):
    answer = 0
    new = []
    if sum(works) < n: # 총 작업량을 퇴근시간전까지 마무리할 수 있는경우 0 리턴
        return 0

    for i in works:     # 최대 힙으로 변경하기 위해 모든 작업량에 대해 -(음수)로 변경
        new.append(-i)
    heapq.heapify(new)  # 힙 적용

    for i in range(n):
        num = heapq.heappop(new)    # 실제로 가장 큰 작업량(힙에선 가장 작은)을 뽑고
        num += 1                    # 뽑은 작업량에 +1을 해준뒤 다시 힙에 추가
        heapq.heappush(new,num)     # 총 n 번 반복

    for i in new:
        answer += i**2              # 남은 일일 작업량에 제곱한 값 = 야근 피로도

    return answer