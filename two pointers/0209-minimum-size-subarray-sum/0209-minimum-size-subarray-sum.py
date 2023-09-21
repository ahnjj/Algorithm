class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        total = 0
        left = 0
        res = len(nums) + 1

        for i in range(len(nums)):
            total += nums[i]

            while total >= target:
                res = min(res, i-left+1)
                total -= nums[left]
                left += 1

        return 0 if res == len(nums) + 1 else res