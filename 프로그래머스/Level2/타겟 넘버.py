from collections import deque


def solution(numbers, target):
    answer = 0
    q = deque()
    q.append([0, 0])  # [현재까지 합, 인덱스]

    while q:
        num, idx = q.popleft()  # num: 현재까지의 합, idx: 인덱스
        if idx == len(numbers):  # 만약 인덱스가 numbers의 길이와 같을 경우 = 마지막 숫자까지 모두 더하거나 뺀 경우
            if num == target:  # 현재까지의 합이 target과 같다면 정답 + 1 카운트
                answer += 1
        else:
            a = numbers[idx]  # a: 현재 인덱스의 값
            q.append([num + a, idx + 1])  # 현재까지의 합에 +a, -a를 해주고 인덱스를 +1을 해준 값을 각각 추가
            q.append([num - a, idx + 1])

    return answer