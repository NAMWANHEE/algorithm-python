def solution(phone_book):
    answer = True
    phone_book.sort()                       # 번호가 작은 순(숫자가 작은 순이 아님)으로 정렬
    for i in range(len(phone_book) - 1):    # 맨마지막 번호 전까지 반복
        l = len(phone_book[i])              # 현재 번호의 길이
        if phone_book[i] == phone_book[i + 1][:l]:  # 다음 숫자는 현재숫자의 자리수까지만 구하여 비교
            answer = False                          # 같으면 answer = False 로 변경 후 반복 종료
            break

    return answer

