class Solution:
    def minSwaps(self, s: str) -> int:
        s = list(s)
        l, r = 0, len(s) - 1
        swap = 0
        open = 0

        while l < r:
            if s[l] == '[':
                open += 1
                l += 1
            else:
                if open > 0 :
                    open -= 1
                    l += 1
                else:
                    while s[r] == ']':
                        r -= 1
                    if r > l:
                        s[l], s[r] = s[r], s[l]
                        r -= 1
                        l += 1
                        swap += 1
                        open += 1
                    else:
                        break

        
        return swap