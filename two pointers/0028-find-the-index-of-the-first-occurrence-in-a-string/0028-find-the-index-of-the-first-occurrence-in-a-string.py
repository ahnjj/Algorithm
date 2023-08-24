class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        for idx, i in enumerate(haystack):
            if i!=needle[0]:
                continue
            if haystack[idx:idx+len(needle)] == needle:
                return idx
        
        return -1