class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        count = 0
        curSum = sum(arr[0:k-1])
        for i in range(len(arr)-k+1):
            curSum += arr[i+k-1]
            if curSum >= threshold*k:
                    count += 1
            curSum -= arr[i]

        return count