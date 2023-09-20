class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        l, r = 0, n-1

        while l < r:
            m = (l+r)//2
            if nums[m] == m:
                l = m + 1
            elif nums[m] > m:
                r = m
        return l if n in nums else n
    