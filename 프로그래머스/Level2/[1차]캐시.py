def solution(cacheSize, cities):
    answer = 0
    if cacheSize == 0:  # 캐시크기가 0인경우 모든 경우가 cache miss 이므로 x5
        return len(cities) * 5
    cache = []

    for i in cities:
        city = i.lower()  # 도시 이름은 대소문자를 구별하지 않으므로 모두 소문자 or 대문자로 변경하여 진행
        if city in cache:  # 도시가 캐시에 있을 경우
            cache.pop(cache.index(city))  # LRU 알고리즘이므로 해당 도시를 캐시에서 빼주고
            cache.append(city)  # 캐시에 해당 도시를 다시 추가하여 가장 최근에 들어온 도시로 만들어줌
            answer += 1  # 도시가 캐시에 있었으므로 cache hit  => +1

        else:  # 도시가 캐시에 없는 경우
            if len(cache) == cacheSize:  # 캐시에 들어있는 도시의 개수가 캐시크기와 동일하면
                cache.pop(0)  # 가장 오래된 도시 제거
            cache.append(city)  # 캐시에 해당 도시 추가
            answer += 5  # 캐시에 도시가 없었으므로 cache miss => +5

    return answer