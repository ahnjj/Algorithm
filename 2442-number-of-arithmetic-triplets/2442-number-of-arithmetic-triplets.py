class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        output = 0
        j, k = 1,2
        for i in range(len(nums)-2):
            while k < len(nums) and nums[k] < nums[i] + diff*2:
                k += 1
            while j < k and nums[j] < nums[i] + diff:
                j += 1
            
            if j<k<len(nums) and nums[k] - nums[j] == diff and nums[j] - nums[i] == diff:
                output += 1
            
        
        return output