class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        new = []
        for i in range(max(len(word1), len(word2))):
            if i > len(word1) - 1:
                new.append(word2[i])
            elif i > len(word2) - 1:
                new.append(word1[i])
            else:
                new.append(word1[i])
                new.append(word2[i])
                
        return ''.join(new)