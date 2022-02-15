def solution(board, moves):
    answer = 0
    st = []  # 스택(바구니)
    cnt = 0  # 인형을 뽑은 횟수
    for i in moves: # moves 는 몇번째 열에 인형을 뽑는지 들어있는 리스트 이므로 i 는 인형뽑는 열(col) 의미
        for j in range(len(board)): # j 는 행(row)를 의미
            if board[j][i - 1] != 0: # 해당열의 맨위의 칸(row) 이 0이 아니라면(비어있지않다면)
                cnt += 1             # 인형 뽑아 옮김 , 카운트 +1
                if st:               # 바구니에 인형이 들어있을 경우
                    if st[-1] == board[j][i - 1]: # 바구니의 맨위 인형과 뽑은 인형이 동일하다면
                        board[j][i - 1] = 0       # 원래 인형이 있던 위치 0으로 변경
                        st.pop()                  # 인형을 바구니에 넣지않고 연속되므로 기존 바구니에서 pop
                        break                     # 다음 인형뽑기 진행

                st.append(board[j][i - 1])        # 바구니의 맨위 인형과 다르다면 바구니에 인형 추가
                board[j][i - 1] = 0               # 원래 인형이 있던 위치 0으로 변경
                break                             # 다음 인형뽑기 진행

    answer = cnt - len(st)                        #  사라져 없어진 인형의 수 = 인형을 뽑은 횟수 - 현재 바구니에 들어있는 인형의 개수
    return answer