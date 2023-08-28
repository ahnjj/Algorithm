class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        output = []
        curc, befc = 0, len(s)-1
        slow = 0
        for fast, v in enumerate(s):
            if v == c:
                curc = fast
                while slow <= fast:
                    output.append(min(abs(befc - slow), abs(curc - slow)))
                    slow += 1
                befc = curc

        if slow <= len(s)-1 and slow > curc:
            while slow <= len(s)-1:
                output.append(abs(curc - slow))
                slow +=1
            
                
        return output
                
        
