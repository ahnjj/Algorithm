class Solution:
    def isValid(self, s: str) -> bool:
        stk = list(s)
        tmp = []

        for i in range(len(stk)):
            if not tmp:
                if (stk[-1] not in [')',']','}']):
                    return False
                else:
                    tmp.append(stk.pop())
            else:
                if stk[-1] in [')',']','}']:
                    tmp.append(stk.pop())
                else:
                    if tmp[-1] == ')':
                        if stk.pop() == '(':
                            tmp.pop()
                        else:
                            return False
                    elif tmp[-1] == ']' :
                        if stk.pop() == '[':
                            tmp.pop()
                        else:
                            return False
                    elif tmp[-1] == '}':
                        if stk.pop() == '{':
                            tmp.pop()
                        else:
                            return False
        
        return True if not(tmp or stk) else False
                
            
