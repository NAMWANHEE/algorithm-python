def solution(record):
    answer = []
    dic = {}
    for i in record:
        if i.split(' ')[0] != 'Leave':               # 기록중에 채팅방을 떠난경우 빼고
            dic[i.split(' ')[1]] = i.split(' ')[2]   # {아이디 : 닉네임} 으로 사전생성

    for i in record:                                                # 변경을 제외한 기록중에
        if i.split(' ')[0] == 'Enter':                              # 참여시 해당 아이디에 대한 닉네임을 위에만든 사전에서 찾아서
            answer.append(dic[i.split(' ')[1]] + '님이 들어왔습니다.') # 메시지를 리스트에 저장
        elif i.split(' ')[0] == 'Leave':
            answer.append(dic[i.split(' ')[1]] + '님이 나갔습니다.')   # 위와 동일하게 채팅방을 떠난경우 메시지 저장

    return answer