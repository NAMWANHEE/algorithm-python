from collections import deque
def solution(people, limit):
    answer = 0
    people = deque(sorted(people,reverse=True)) # 사람들의 몸무게 순으로 정렬
    while people:  # 구명보트에 사람이 있다면 계속 반복
        if len(people) == 1:    # 보트에 사람이 1명있을 경우
            people.pop()        # 혼자 이동(pop)
            answer += 1         # 카운트 +1
            break               # 보트에 사람이 0명되므로 종료
        if people[0] + people[-1] > limit:  # 가장 가벼운사람과 가장 무거운 사람의 몸무게의 합이 한계치를 넘을 경우
            people.popleft()                # 가장 무거운 사람만 이동(pop)
            answer += 1                     # 카운트 + 1
        elif people[0] + people[-1] <= limit:   # 가장 무겁고 가벼운 무게의 합이 한계치 이하일때
            people.popleft()                    # 두명다 이동 (pop)
            people.pop()
            answer += 1                         # 카운트 + 1
    return answer