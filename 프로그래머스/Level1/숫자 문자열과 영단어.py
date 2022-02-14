def solution(s):
    answer = ''
    a = '' # 숫자 영단어가 충족될때까지 담아두는곳
    dic = {}
    word = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    for i in range(10):
        dic[word[i]] = str(i) # {'영단어' : '숫자'} 생성

    for i in s:  # s: 주어진 문자열
        try:            # 만약에 영단어가아닌 숫자가 주어지면
            int(i)      # 정답에 추가
            answer += i
            continue    # 다음반복
        except:
            pass

        a += i          # 문자가 나오면 임시로 a 에 계속 담아두고
        if a in word:   # 계속 담아둔 문자가 word(숫자영단어)에 있으면
            answer += dic[a]     # 사전에서 해당 영단어에 대응되는 숫자를 정답에 추가
            a = ''               # 임시로 담아두는 a 문자열 초기화
    answer = int(answer)
    return answer