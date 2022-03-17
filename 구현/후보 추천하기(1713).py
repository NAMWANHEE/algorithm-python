from collections import defaultdict, deque

n = int(input())  # 사진틀의 개수
m = int(input())  # 전체 학생의 총 추천 횟수
photo = deque()  # 사진틀담을 데크
dic = defaultdict(int)  # 학생의 추천 횟수 담을 딕셔너리
re = list(map(int, input().split()))  # 추천받은 학생을 나타내는 번호

for i in re:
    if len(photo) == n:  # 사진틀의 개수가 꽉찼을때
        if i in photo:  # 사진틀에 추천받은 학생이 이미 존재할 경우
            dic[i] += 1  # 추천 횟수 +1
            continue  # 다음 학생 번호로 넘어감

        re_min = min(list(dic.values()))  # 추천 받은 학생중 최소의 추천 개수
        for j in range(n):  # 모든 사진틀에 대해
            if dic[photo[j]] == re_min:  # 해당 학생의 추천 수가 최소의 추천 개수와 같을 경우
                del dic[photo[j]]  # 해당 학생 추천개수 담는 딕셔너리에서 제거
                del photo[j]  # 해당 학생 사진틀에서 제거
                break  # 반복문 종료

        photo.append(i)  # 현재 학생 추가
        dic[i] += 1  # 현재 학생 추천수 +1

    else:  # 사진틀이 비어있는 경우가 있을때
        if i in photo:  # 학생이 이미 사진틀에 있는 경우
            dic[i] += 1  # 추천수만 +1
        else:
            photo.append(i)  # 학생이 사진틀에 없을 경우 사진틀에 추가 후 추천수 +1
            dic[i] += 1

print(*sorted(photo))
