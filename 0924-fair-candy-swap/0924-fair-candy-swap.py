class Solution:
    def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
        s1 = sum(aliceSizes)
        s2 = sum(bobSizes)

        def binary_search(A, B):
            B.sort()

            for box1 in A:
                l, r = 0, len(B)-1
                box2 = (2 * box1 + abs(s2 - s1))//2
                while l<=r:
                    m = (l+r)//2
                    if B[m] > box2:
                        r = m - 1
                    elif B[m] < box2:
                        l = m + 1
                    else:
                        return [box1, box2]


        if s1 > s2:
            output = binary_search(bobSizes, aliceSizes)
            return output[::-1]
        else:
            return binary_search(aliceSizes, bobSizes)
