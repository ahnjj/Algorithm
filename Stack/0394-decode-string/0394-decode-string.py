class Solution:
    def decodeString(self, s: str) -> str:
        nested,num = "",0
        stack = []
        for v in s:
            if v.isdigit():
                num = num*10+int(v)
            elif v == '[':
                stack.append(nested)
                stack.append(num)
                nested = ''
                num = 0
            elif v == ']':
                repeat = stack.pop()
                before = stack.pop()
                nested = before + repeat*nested
            else:
                nested += v
                
        return nested
            