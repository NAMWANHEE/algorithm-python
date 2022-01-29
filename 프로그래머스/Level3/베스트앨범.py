def solution(genres, plays):
    a = {}  # {장르 : 해당 장르 총 재생수}
    b = []  # [곡의 장르, 재생수, 노래 고유번호]
    ans = []
    for i in range(len(plays)):
        try:                                    # 사전에 이미 노래 장르가 있는경우
            b.append([genres[i],plays[i],i])    # 리스트에 장르와 재생수, 고유번호 기록
            a[genres[i]] += plays[i]            # 사전에 기존 장르의 재생수에 더해줌
        except:                                 # 사전에 노래 장르가 없는 경우
            a[genres[i]] = plays[i]             # 사전에 장르와 재생수 추가
    a1 = sorted(a.items(), key=lambda x: x[1], reverse=True) # 재생수가 많은 장르부터 정렬
    b2 = sorted(b,key=lambda x: x[1], reverse=True)          # 재생수에 따라 모든 노래 정렬
    for i in a1:    # 장르별로 반복

        c=0         # 한 장르당 top2 까지만 저장하기 위해 카운트할 변수
        for j in b2:    # 모든 노래에 대해 반복
            if c == 2:  # 카운트가 2가 될시 다음 장르로 넘어감
                break
            if i[0] == j[0]:        # 노래의 장르가 일치할경우
                ans.append(j[2])    # 정답에 해당 노래의 고유번호 추가
                c += 1              # 해당 장르 개수 카운팅
    return ans