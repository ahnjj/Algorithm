class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        output = 0
        j,k = False, False
        i = 0
        while i + 2 < len(nums):
            for x in range(i, len(nums)):
                if nums[x] == nums[i] + diff:
                    j = True
                if nums[x] == nums[i] + diff*2:
                    k = True
            
            if j and k:
                output += 1
            i+=1
            k,j = 0,0

        return output