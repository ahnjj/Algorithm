class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        nums.sort()

        i, j = 0, len(nums)-1
        while(i<j):
            if nums[i] == -nums[j]:
                return nums[j]
            elif -nums[i] < nums[j]:
                j -= 1
            elif -nums[i] > nums[j]:
                i += 1

        return -1

