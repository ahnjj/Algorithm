class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        soldiers = dict()

        def count(arr):
            l, r = 0, len(arr)-1
            while l<=r:
                m = (l+r)//2
                if arr[m] == 1:
                    l = m + 1
                else:
                    r = m - 1
            return l

        # l = soldiers number
        for i, row in enumerate(mat):
            soldiers[i] = count(row)

        # sort by weakness
        res = sorted(soldiers.items(), key = lambda item : (item[1],item[0]))

        return [res[i][0] for i in range(k)]
            