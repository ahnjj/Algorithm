class Solution:
    def reverseWords(self, s: str) -> str:
        answer = []
        for i in s.split():
            l, r = 0, len(i)-1
            new = list(i)
            while l<r:
                new[l], new[r] = new[r], new[l]
                l += 1
                r -= 1
            answer.append(''.join(new))

            
        return ' '.join(answer)