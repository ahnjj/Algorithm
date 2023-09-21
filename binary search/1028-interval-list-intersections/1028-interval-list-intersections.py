class Solution:
    def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        output = []
        a, b = 0, 0

        while a < len(A) and b < len(B) :
            a_start, a_end = A[a][0], A[a][1]
            b_start, b_end = B[b][0], B[b][1]
            
            if a_start <= b_end and b_start <= a_end:
                output.append([max(a_start,b_start), min(a_end,b_end)])
            
            if a_end <= b_end:
                a += 1
            else:
                b += 1


        return output