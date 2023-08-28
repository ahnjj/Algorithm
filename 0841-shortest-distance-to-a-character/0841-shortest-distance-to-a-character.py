class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        befc = float('-inf')
        output = []

        for i, x in enumerate(s):
                if x == c:
                        befc = i
                output.append(i-befc)

        befc = float('inf')
        for i in range(len(s)-1, -1, -1):
                if s[i] == c:
                        befc = i
                output[i] = min(output[i], befc-i)
        
        return output
                
        
