class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        output = 0
        nums_dict = {}

        for i in range(len(nums)):
            nums_dict[i] = nums[i]

        for i in nums_dict.keys():
            for j in range(i+1, len(nums_dict)):
                if nums[i] == nums[j]:
                    output += 1

        return output