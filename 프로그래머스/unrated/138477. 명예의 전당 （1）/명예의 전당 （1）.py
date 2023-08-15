def solution(k, score):
    hall = []
    lowest = []
    for singer in score:
        if len(hall) < k:
            hall.append(singer)
        else:
            if singer > min(hall):
                hall.append(singer)
                hall.sort(reverse= True)
                hall = hall[:k]    
        lowest.append(min(hall))

    return lowest