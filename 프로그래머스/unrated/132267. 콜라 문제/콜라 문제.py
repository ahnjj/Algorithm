def solution(a, b, n):
    free = 0
    empty = n

    while empty>=a:
        free += (empty//a)*b
        empty = (empty//a)*b + (empty%a)
    return free