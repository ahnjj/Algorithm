class Solution:
    def isValid(self, s: str) -> bool:
        stk = []
        opened = ['[', '(', '{']
        closed = [']', ')', '}']

        for i in s:
            if i in opened:
                stk.append(i)
            else:
                if len(stk) != 0 and opened[closed.index(i)] == stk[-1]:
                    stk.pop()
                else:
                    return False
        
        return False if stk else True
                
            
