def solution(ingredient):
    hamburger = 0
    
    if len(ingredient) >= 4:
        kitchen = ingredient[0:3]
        for i in ingredient[3:]:
            kitchen.append(i)

            if kitchen[-4:] == [1,2,3,1]:
                hamburger += 1
                for i in range(4):
                    kitchen.pop()
    
    return hamburger