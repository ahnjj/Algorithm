class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)-1):
            if i % 2 == 0 :
                if nums[i] % 2 != 0:
                    j = i + 1
                    while j < len(nums):
                        if nums[j] % 2 == 0:
                            nums[i], nums[j] = nums[j], nums[i]
                            break
                        j += 1
            else:
                if nums[i] % 2 == 0:
                    j = i + 1
                    while j < len(nums):
                        if nums[j] % 2 != 0:
                            nums[i], nums[j] = nums[j], nums[i]
                            break
                        j += 1

        return nums