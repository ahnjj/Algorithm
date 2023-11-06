class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        group_d = {i:groupSizes[i] for i in range(len(groupSizes)) }
        group_d = dict(sorted(group_d.items(), key = lambda x:x[1]))

        res = []
        cur = []
        cnt = -1

        for p,c in group_d.items():
            if cnt == -1:
                cnt = c - 1  # initialize
            else:
                cnt -= 1
            if cnt == 0 :
                cur.append(p)
                res.append(cur)
                cur = [] # initialize
                cnt = -1 # initialize
            else:
                cur.append(p)


        return res