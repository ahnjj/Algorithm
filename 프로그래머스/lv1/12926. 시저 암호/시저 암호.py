def solution(s, n):
    ans = ''
    for i in s:
        if ord(i) == 32:
            ans += ' '
        elif (ord(i) <= 90 and ord(i) + n > 90) or (ord(i) >= 97 and ord(i) + n > 122):
            ans += chr(ord(i) + n - 26)
        else: ans += chr(ord(i) + n)

    return ans