class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        n = len(nums)
        l, r = 0, n-1
        neg = pos = 0

        # leftmost - last neg
        while l <= r:
            m = (l+r)//2
            if nums[m] < 0 :
                neg = m + 1
                l = m + 1
            else:
                r = m - 1

        l, r = 0, len(nums)-1
        while l <= r:
            m = (l+r)//2
            if nums[m] > 0:
                pos = n - m
                r = m - 1
            else:
                l = m + 1
                
        return max(neg, pos)
