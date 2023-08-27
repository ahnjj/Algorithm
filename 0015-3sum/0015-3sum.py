class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        output = set()
        nums.sort()
        n = len(nums)

        for i in range(0,n-2):
            if nums[i] == nums[i-1] and i > 0:
                continue
            j = i+1
            k = n-1
            while j < k: 
                if nums[j] + nums[k] == -(nums[i]):
                    output.add((nums[i], nums[j], nums[k]))
                    k -= 1
                    j += 1
                elif  nums[j] + nums[k] > -(nums[i]):
                    k -= 1
                elif  nums[j] + nums[k] < -(nums[i]):
                    j += 1
            

            
        return output 
