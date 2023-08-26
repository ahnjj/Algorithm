class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i, j = 0, 0
        m, n = len(word1), len(word2)
        result = []
        while i < m or j < n:
            if i < m:
                result.append(word1[i])
                i += 1
            if j < n:
                result.append(word2[j])
                j += 1

        return ''.join(result)			