class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        left = right = -1
        #1 sorting
        nums.sort()

        # leftmost index
        l, h = 0, len(nums)-1
        while l <= h:
            mid = (l+h)>>1
            if nums[mid] == target:
                left = mid
                h = mid - 1
            elif nums[mid] > target:
                h = mid - 1
            else:
                l = mid + 1
            
        # rightmost index
        l, h = left, len(nums)-1
        while l <= h:
            mid = (l+h)>>1
            if nums[mid] == target:
                right = mid
                l = mid + 1
            elif nums[mid] > target:
                h = mid - 1
            else:
                l = mid + 1

        if left == -1:
            return []
        ans=range(left,right+1)
        return ans 