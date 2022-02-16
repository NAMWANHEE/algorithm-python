def solution(w,h):

    def x(i):
        return int((-(h/w)*i) + h) # 가로와 세로를 가지고 대각선의 기울기를 이용하여 직선의 방정식을 만들고
                                   # 해당 직선의 방정식에 x 축 좌표(i) 를 넣어주고 int 형으로 정수로 바꿔주면 사용가능한 정사각형의 개수만 리턴해주게 된다
    answer = 0
    a = w*h   # 전체 정사각형의 개수

    if w == h:                 # 가로, 세로가 같을경우 정답은 (전체 정사각형 개수) - (가로 or 세로의 수)
        answer = a-w

    elif w ==1 or h == 1:      # 가로나 세로가 둘중 하나라도 1일 경우 모든 정사각형 사용 불가
        answer = 0

    else:
        for i in range(1,w):   # 반복문의 범위를 1부터 w-1까지 설정해준다, w일때는 어차피 무조건 0
            answer += x(i)     # 위에서 만든 함수에 x축 좌표 (i)를 반복문에 따라 넣고 결과를 answer에 축적
        answer *= 2            # 정답은 대각선의 위아래 대칭이기 때문에 곱하기 2를 해준다
    return answer