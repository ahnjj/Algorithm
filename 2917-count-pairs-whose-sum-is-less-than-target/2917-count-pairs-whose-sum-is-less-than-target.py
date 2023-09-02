class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        nums.sort()
        i, output = 0, 0

        while i < len(nums) - 1:
            j = i + 1
            while j < len(nums):
                if nums[j] < target - nums[i]:
                    output += 1
                    j += 1
                else: 
                    break
            i += 1

        return output