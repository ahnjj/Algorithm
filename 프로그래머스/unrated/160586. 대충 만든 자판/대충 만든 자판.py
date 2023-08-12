def solution(keymap, targets):
    key_dict = {}

    for i in keymap:
        for idx, char in enumerate(i):
            if char not in key_dict:
                key_dict[char] = idx+1
            else:
                key_dict[char] = min(key_dict[char], idx+1)

    key_set = set(key_dict.keys())

    answer = []             
    for j in targets:
        if not(set(j) - key_set):
            answer.append(sum(key_dict[char] for char in j))
        else:
            answer.append(-1)
    return answer