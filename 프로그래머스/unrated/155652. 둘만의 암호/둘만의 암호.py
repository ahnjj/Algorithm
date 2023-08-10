def solution(s, skip, index):
    new = ''

    def al(n):
        return ((n-97)%26)+97

    for c in s:
        count = 0
        start = ord(c) 
        while count < index:
            if chr(al(start+1)) not in skip:
                count += 1
            start += 1

        new += chr(al(start))
    return new