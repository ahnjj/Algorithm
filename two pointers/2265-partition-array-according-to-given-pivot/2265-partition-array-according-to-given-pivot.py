class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        g = []
        pcount, last = 0, 0

        for i in range(len(nums)):
            if nums[i] > pivot:
                g.append(nums[i])
            elif nums[i] < pivot:
                nums[i], nums[last] = nums[last], nums[i]
                last += 1
            elif nums[i] == pivot:
                pcount += 1

        g_idx =0 

        while last < len(nums):
            if pcount > 0:
                nums[last] = pivot
                last += 1
                pcount -= 1
            else:
                nums[last] = g[g_idx]
                g_idx += 1
                last += 1

                
        return nums