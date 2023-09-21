class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        sub = ''
        for size in range(2, len(s)+1):
            for start in range(len(s)-size+1):
                window = s[start:start+size]
                check = True
                for i in window:
                    if not((i.isupper() and i.lower() in window) or (i.islower() and i.upper() in window)):
                        check = False
                        break
                if check == True:
                    sub = window
                    break

        return sub
                