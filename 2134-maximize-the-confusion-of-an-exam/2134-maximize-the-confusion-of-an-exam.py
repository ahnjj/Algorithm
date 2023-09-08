class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:

        numT = numF = 0
        start = 0
        res = 1

        for end in range(len(answerKey)):
            if answerKey[end] == 'T':
                numT += 1
            else:
                numF += 1
            
            while numT > k and numF > k:
                if answerKey[start] == 'T':
                    numT -= 1
                else:
                    numF -= 1
                start += 1

            res = max(res, end-start +1)

        return res
            