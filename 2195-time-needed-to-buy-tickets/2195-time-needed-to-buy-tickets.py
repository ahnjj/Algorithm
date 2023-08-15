class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        q = []

        while any(tickets):
            for idx, t in enumerate(tickets):
                if t != 0:
                    q.append(idx)
                    tickets[idx] -= 1

        final_index = max([idx for idx, p in enumerate(q) if p == k])
        return final_index+1
