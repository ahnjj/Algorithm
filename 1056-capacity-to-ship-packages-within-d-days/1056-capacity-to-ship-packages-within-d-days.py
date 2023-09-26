class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
                
        left = max(weights)
        right = sum(weights)

        while left < right:
            mid = (left+right) // 2
            currDay, currWeight = 1, 0
            for weight in weights:
                if currWeight + weight > mid:
                    currDay += 1
                    currWeight = 0
                currWeight += weight
            if currDay > days:
                left = mid + 1
            else:
                right = mid
        return left