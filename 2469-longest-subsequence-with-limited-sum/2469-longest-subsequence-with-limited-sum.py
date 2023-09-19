class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        nums.sort()
        ans = []

        for q in queries:
            cur = length = i = 0
            target = q
            
            while i < len(nums):
                cur += nums[i]
                if cur <= target:
                    length += 1
                else:
                    print(i, 'break')
                    break
                i += 1
                
            ans.append(length)

        return ans

