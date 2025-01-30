def solution(clothes):
    clothes_dict = {} #종류별로 의상 분류
    for item, category in clothes:
        if category not in clothes_dict:
            clothes_dict[category] = []
        clothes_dict[category].append(item)
    
    answer = 1
    for category in clothes_dict.values():#카테고리에 따른 값 리스트 반환
        answer *= (len(category) + 1) #선택을 하지 않은 경우도 있기 때문에 +1
        
    answer -= 1 #옷을 아예 아무것도 입지 않은 경우 제외
    return answer