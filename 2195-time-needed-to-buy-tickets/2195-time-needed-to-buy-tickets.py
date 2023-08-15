class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        q = collections.deque()
        goal = tickets[k]
        while any(tickets):
            for idx, t in enumerate(tickets):
                if t != 0:
                    q.append(idx)
                    tickets[idx] -= 1

        cnt = 0
        line = len(q)
        while cnt != goal:
            if q.popleft() == k:
                cnt += 1
                if cnt == goal:
                    return line - len(q)