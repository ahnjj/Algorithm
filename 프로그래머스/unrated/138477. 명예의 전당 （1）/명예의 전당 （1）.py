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

# sort / slicing은 원소 길이가 길어지면 비효율적이다.
# Queue(FINFO)를 사용하라

    q = []
    lowest = []
    for singer in score:
        q.append(singer)
        if len(q) > k:
            q.remove(min(q))
    
        lowest.append(min(q))
    return lowest
