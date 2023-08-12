def solution(keymap, targets):
    key_dict = {}
    answer = []

    for i in keymap:
        for idx, char in enumerate(i):
            if char not in key_dict:
                key_dict[char] = idx+1
            else:
                key_dict[char] = min(key_dict[char], idx+1)
                
# 굳이 set 변수를 또 만들기 + append 함수 반복 활용 필요 없음 ... 아래에 코드 첨부
    key_set = set(key_dict.keys())
  
    for j in targets:
        if not(set(j) - key_set):
            answer.append(sum(key_dict[char] for char in j))
        else:
            answer.append(-1)
    return answer
------------------------------------------------------------
# for 먼저 돌리고 if 하면 됌    
    for j in targets:
        ret = 0
        for char in j:
            if char in key_dict:
                ret += key_dict[char]
            else:
                ret = -1  
        answer.append(ret)
        
    return answer
