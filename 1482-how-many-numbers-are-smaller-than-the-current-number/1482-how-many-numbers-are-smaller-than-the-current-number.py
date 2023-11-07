class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        n = len(nums)
        output = [0 for _ in range(n)]
        for i in range(n):
            for j in range(n):
                if nums[i] > nums[j]:
                    output[i] += 1
        return output