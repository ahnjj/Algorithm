class Solution:
    def findTheArrayConcVal(self, nums: List[int]) -> int:
        l = 0
        r = len(nums)-1
        con = 0

        while l <= r:
            if l != r:
                con += int(str(nums[l]) + str(nums[r]))
            else:
                con += nums[l]
            l += 1
            r -= 1
        
        return con