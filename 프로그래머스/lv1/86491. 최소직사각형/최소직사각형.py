def solution(sizes):
    w = [min(i,v) for i,v in sizes]
    d = [max(i,v) for i,v in sizes]
    return max(w) * max(d)