def solution(skill, skill_trees):
    answer = 0
    skill_list = [''] # 배울수 있는 스킬트리를 담을 리스트 , '' 빈문자열을 추가한 이유는 선행 스킬이 필요없는 스킬일 경우를 생각하기위해

    a = ''
    for i in skill: # skill 의 맨처음 스킬부터 하나씩 추가해주며 배울수 있는 스킬트리 추가
        a += i      # ex) skill : "CBD" 라면 ['C','CB','CBD']를 추가
        skill_list.append(a)

    for i in skill_trees:
        sp = ''
        for j in i:
            if j in skill:  # 해당 스킬트리의 스킬중 선행 스킬이 필요한 경우 sp에 더해줌
                sp += j

        if sp in skill_list:    # sp가 배울수 있는 스킬트리에 있다면 정답 +1 추가
            answer += 1

    return answer
