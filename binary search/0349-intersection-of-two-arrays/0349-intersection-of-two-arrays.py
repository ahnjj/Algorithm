class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()

        def search(arr,target):
            l,r = 0, len(arr)-1
            
            while l<=r:
                m = (l+r)//2
                if arr[m] > target:
                    r = m - 1
                elif arr[m] < target:
                    l = m + 1
                else:
                    return True
            return False

        def result(arr1, arr2):
            ans = []
            for target in arr1:
                if search(arr2,target) and target not in ans:
                    ans.append(target)
            return ans

        if len(nums1) > len(nums2):
            return result(nums2,nums1)
        else:
            return result(nums1,nums2)