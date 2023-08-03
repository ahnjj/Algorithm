def solution(s):
# 방법1. dict -> replace multiple times
    replacements = {'zero':'0','one': '1', 'two':'2', 'three':'3', 'four':'4', 'five':'5', 'six':'6', 'seven':'7', 'eight':'8', 'nine':'9'}

    for k,v in replacements.items():
        if k in s:
            s = s.replace(k,v)
    return int(s)


# runtime error
# 방법2. nested replace

# 방법3. re.sub + dict
# import re
# replacements = {'one': '1', 'two':'2', 'three':'3', 'four':'4', 'five':'5', 'six':'6', 'seven':'7', 'eight':'8', 'nine':'9'}

# for code in replacements:
#     s = re.sub(code,replacements.get(code),s)
