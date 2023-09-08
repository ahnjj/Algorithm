class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        def changeTo(target):
            start = 0
            change = 0
            res = 1
            
            for end in range(len(answerKey)):
                if answerKey[end] == target:
                    
                    change += 1       
                    while change > k:
                        if answerKey[start] == target:
                            change -= 1
                        start += 1 
                res = max(res, end-start+1)
            return res


        return max(changeTo('T'), changeTo('F'))
