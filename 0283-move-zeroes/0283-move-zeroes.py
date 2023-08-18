class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        for ptr0 in range(len(nums)):
            if nums[ptr0] == 0:
                for ptrn in range(ptr0+1, len(nums)):
                    if nums[ptrn] != 0:
                        nums[ptr0] = nums[ptrn]
                        nums[ptrn] = 0
                        break
            else:
                continue
        return nums