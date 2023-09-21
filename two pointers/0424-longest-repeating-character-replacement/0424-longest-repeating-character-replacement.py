class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        start = 0
        res = 1
        targets = {}
        for end in range(len(s)):
            if s[end] not in targets:
                targets[s[end]] = 0
            targets[s[end]] += 1
            cur = end - start + 1
            if cur - max(targets.values()) <= k:
                res = max(res, cur)
            else:
                targets[s[start]] -= 1
                if not targets[s[start]]:
                    targets.pop(s[start])
                start += 1
            
        return res