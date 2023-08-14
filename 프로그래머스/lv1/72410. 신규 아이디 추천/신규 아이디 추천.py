def solution(new_id):
    ans = ''
    import re
    new_id = new_id.lower()
    ans =re.sub('[^a-z0-9\-_.]','', new_id)
    ans = re.sub('\.+','.',ans)
    ans = re.sub('^[.]','',ans)
    if ans == '':
        ans += 'a'

    ans = ans[:15]
    ans = re.sub('[.]$','',ans)

    if len(ans) <= 2:
        ans += ans[-1]*(3-len(ans))

    return ans