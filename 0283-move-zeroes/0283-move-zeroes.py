class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        ptr0 = 0
        for ptrn in range(len(nums)):
            if nums[ptrn] != 0:
                nums[ptr0], nums[ptrn] = nums[ptrn], nums[ptr0]
                ptr0 += 1

        return nums