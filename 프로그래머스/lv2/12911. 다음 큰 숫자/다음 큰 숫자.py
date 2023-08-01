def solution(n):
    ans = n + 1
    cnt = str(bin(n)).lstrip('0b').count('1')

    while ans <= 1000000:
        if str(bin(ans)).lstrip('0b').count('1') == cnt:
            break
        ans += 1

    return ans