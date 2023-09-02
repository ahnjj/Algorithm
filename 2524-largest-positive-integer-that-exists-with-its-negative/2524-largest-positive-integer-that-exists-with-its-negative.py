class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        curLar = -1

        for i in range(0,len(nums)-1):
            if curLar <= abs(nums[i]):
                j = i+1
                while j<len(nums):
                    if nums[j] == nums[i]*(-1):
                        curLar = abs(nums[i])
                        break
                    j += 1
                    
        return curLar
