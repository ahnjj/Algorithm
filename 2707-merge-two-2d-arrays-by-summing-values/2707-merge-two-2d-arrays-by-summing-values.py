class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        res = []
        a, b = 0, 0
        
        while a < len(nums1) or b < len(nums2):
            if a >= len(nums1) or b >= len(nums2):
                if b >= len(nums2):
                    res.append([nums1[a][0],nums1[a][1]])
                    a += 1
                else:
                    res.append([nums2[b][0],nums2[b][1]])
                    b += 1
            else:
                if nums1[a][0] == nums2[b][0]:
                    res.append([nums1[a][0],nums1[a][1] + nums2[b][1]])
                    a += 1
                    b += 1
                elif nums1[a][0] < nums2[b][0]:
                    res.append([nums1[a][0],nums1[a][1]])
                    a += 1
                elif nums1[a][0] > nums2[b][0]:
                    res.append([nums2[b][0],nums2[b][1]])
                    b += 1

        return res
            