class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        l, r = 0, len(nums)-1
        new = list(range(len(nums)))
        idx = len(nums)-1
        while -1 < r and idx > -1:
            if abs(nums[l]) < abs(nums[r]):
                new[idx] = nums[r] * nums[r]
                r -= 1
            else:
                new[idx] = nums[l] * nums[l]
                l += 1
            idx -= 1
        return new