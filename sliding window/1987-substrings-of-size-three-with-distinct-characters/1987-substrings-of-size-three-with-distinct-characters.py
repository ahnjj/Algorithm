class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        good = 0
        for i in range(len(s)-2):
            if len(s[i:i+3]) == len(set(s[i:i+3])):
                good += 1

        return good