class Solution:
    def maxArea(self, height: List[int]) -> int:
        cur_max = 0
        left, right = 0,len(height)-1

        while left<=right:
            area = (right - left)*min(height[left],height[right])
            cur_max = max(cur_max,area)
            if height[left] <= height[right]:
                left+= 1
            else:
                right-=1
        return cur_max