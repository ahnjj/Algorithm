def solution(n):
    ans = n + 1
    cnt = str(bin(n)).lstrip('0b').count('1')

    while ans <= 1000000:
        if str(bin(ans)).lstrip('0b').count('1') == cnt:
            break
        ans += 1

    return ans


# 리뷰 : 더 간단 / 적은 변수 사용하는 방법

def solution(n):
    cnt = bin(n).count('1')

    while n <= 1000000:
        n += 1
        if bin(ans).count('1') == cnt:
            break

    return n
