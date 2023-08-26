class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        n = len(nums)
        while n > 1:
            for s in range(n-1):
                if nums[s] % 2 == 1:
                    nums[s], nums[s+1] = nums[s+1], nums[s]

            n -= 1

        return nums