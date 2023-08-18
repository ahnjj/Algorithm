class Solution:
    def decodeString(self, s: str) -> str:
        stack = []

        for v in s:
            if v != ']':
                stack.append(v)
            elif v == ']':
                alpha = ''
                num = ''
                while (x := stack.pop())!= '[':
                    alpha+=x

                while stack and stack[-1].isdigit():
                    num+= stack.pop()

                new_str = int(num[::-1])*alpha[::-1]
                
                for i in new_str:
                    stack.append(i)
                

        return ''.join(stack)
