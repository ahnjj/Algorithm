def solution(new_id):
    ans = ''
    tmp = ''
    # 1
    new_id = new_id.lower()

    # 2
    for i in new_id:
        if i.isalpha() or i.isdigit() or i in ('-','_', '.'):
            tmp += i


    # 3
    for idx in range(len(tmp)):
        if tmp[idx:idx+2] == '..':
            ans += '.'
        else:
            ans += tmp[idx]
        ans = ans.replace('..','.')

    # 4
    ans = ans.strip('.')

    # 5
    if ans == '':
        ans += 'a'

    # 6
    ans = ans[:15]
    ans = ans.rstrip('.')

    # 7
    if len(ans) <= 2:
        ans += ans[-1]*(3-len(ans))

    return ans