class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        zero = 0
        n = []
        p = []
        
        for num in nums:
            if num < 0:
                p.append(num)
            elif num > 0:
                n.append(num)
            else:
                zero += 1

        output = set()
        N = set(n)
        P = set(p)

        if zero:
            for num in N:
                if (-1)*num in P:
                    output.add((0, num, (-1)*num))
        if zero >= 3:
            output.add((0,0,0))


        for i in range(len(n)):
            for j in range(i+1,len(n)):
                target = -1*(n[i] + n[j])
                if target in P:
                    output.add(tuple(sorted([n[i],n[j],target])))
            
        for i in range(len(p)):
            for j in range(i+1,len(p)):
                target = -1*(p[i]+p[j])
                if target in N:
                    output.add(tuple(sorted([p[i],p[j],target])))

        return output 
