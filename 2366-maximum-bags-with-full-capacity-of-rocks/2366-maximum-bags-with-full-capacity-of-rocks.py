class Solution:
    def maximumBags(self, capacity: List[int], rocks: List[int], additionalRocks: int) -> int:
        leftRocks = []
        for c, r in zip(capacity, rocks):
            leftRocks.append(c-r)

        right = sum(leftRocks)
        left = min(leftRocks)
        maxbag = 0

        while left <= right:
            mid = (left+right)//2
            cur = 0
            bag = 0
            for leftRock in sorted(leftRocks):
                if cur + leftRock <= mid:
                    cur += leftRock
                    bag += 1
                else:
                    break
            if mid > additionalRocks:
                right = mid - 1
            else:
                left = mid + 1
                maxbag = max(bag, maxbag)

        return maxbag