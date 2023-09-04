class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        count = 0
        curSum = sum(arr[0:k])
        for i in range(len(arr)-k+1):
            if curSum >= threshold*k:
                    count += 1
            
            if i + k < len(arr):
                curSum = curSum - arr[i] + arr[i+k]

        return count