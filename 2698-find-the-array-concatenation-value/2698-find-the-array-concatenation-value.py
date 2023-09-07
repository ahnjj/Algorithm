class Solution:
    def findTheArrayConcVal(self, nums: List[int]) -> int:
        l = 0
        r = len(nums)-1
        con = 0

        while l < r:
            con += int(str(nums[l]) + str(nums[r]))
            l += 1
            r -= 1
                
        if len(nums)%2 != 0:
            con += nums[l]
        
        return con
