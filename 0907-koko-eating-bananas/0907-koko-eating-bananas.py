class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        from math import ceil

        left = ceil(sum(piles) / h)   # 1시간에 먹어야하는 최소 바나나수
        right = max(piles)    # 1시간에 먹어야하는 최대 바나나수

        while left < right:  
            mid = (left + right) // 2
            total_time = 0
            for pile in piles:
                total_time += ceil(pile / mid)
                if total_time > h:
                    break
            if total_time <= h: # h일수 있으니 끝(mid)살리고 앞쪽 반
                right = mid 
            else:
                left = mid + 1

        return right