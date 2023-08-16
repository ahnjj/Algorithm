class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        q = list(range(1,n+1))

        while len(q) != 1:
            for i in range(k):
                tmp = q.pop(0)
                q.append(tmp)
            q.pop()

        return q[0]