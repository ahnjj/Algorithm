class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        def changeTo(target):
            start = 0
            res = 1
            change = 0
            
            for end in range(len(s)):
                if s[end] != target:
                    change += 1
                    
                    while change > k:
                        if s[start] != target:
                            change -=1
                        start += 1
                res = max(res, end - start + 1)
            return res
        
        targets = set(s)
        return max(changeTo(target) for target in targets)