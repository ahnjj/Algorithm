class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last = { c : idx for idx, c in enumerate(s) }

        anchor, j = 0, 0
        result = []

        for i, c in enumerate(s):
            j = max(j, last[c])

            if j == i:
                result.append(i-anchor+1)
                anchor = i+1

        return result
        