def solution(n):
    cnt = 0
    a, b = n, 1
    
    while a > 0:
        a = a - b

        if a % b == 0:
            cnt += 1
        b += 1
    
    return cnt
            