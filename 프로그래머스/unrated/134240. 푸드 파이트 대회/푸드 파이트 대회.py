def solution(food):
    left = ''
    for idx, num in enumerate(food):
        left += str(idx) *(num//2)

    return left + '0' + left[::-1]