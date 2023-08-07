def solution(name, yearning, photo):
    nm_yn = {name[i] : yearning[i] for i in range(len(name))}

    return [sum(nm_yn[person] for person in pic if person in name) for pic in photo]
