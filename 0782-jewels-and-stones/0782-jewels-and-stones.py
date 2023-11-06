class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        j_dict = {}
        output = 0

        for i in range(len(jewels)):
            j_dict[i] = jewels[i]

        for c in stones:
            if c in j_dict.values():
                output += 1
        return output