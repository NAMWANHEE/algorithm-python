def solution(n):
    if n <= 3:
        return '124'[n-1] # n이 3이하이면 1일땐 1, 2일땐 2, 3일땐 4
    else:
        a = n % 3      #  나머지가 1,2,0 이 나옴
        b = (n-1) // 3 # 3의 배수일 경우 틀려지는것을 방지
        return solution(b) + '412'[a] # 재귀 + 나머지를 이용해 가장 뒷자리 부터 1,2,4 중 채워나감
    