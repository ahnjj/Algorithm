class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        right = []
        left = []
        pcount = 0

        
        for l in nums:
            if l < pivot:
                left.append(l)
            elif l > pivot:
                right.append(l)
            elif l == pivot:
                pcount += 1
                

        return left + [pivot]*pcount + right