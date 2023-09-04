class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        ch_idx = word.find(ch)
        if ch_idx == -1:
            return word
        else:
            word = list(word)
                
            i = 0
            while i < ch_idx:
                word[i], word[ch_idx] = word[ch_idx], word[i]
                i += 1
                ch_idx -=1
                
        return ''.join(word)