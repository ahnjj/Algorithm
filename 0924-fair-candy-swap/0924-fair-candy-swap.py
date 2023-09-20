class Solution:
    def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
        aliceSizes.sort()
        bobSizes.sort()

        alice = sum(aliceSizes)
        bob = sum(bobSizes)

        for alice_change in aliceSizes:
            bl, br = 0, len(bobSizes)-1
            while bl <= br:
                bm = bl + (br-bl)//2
                bob_change = bobSizes[bm]
                new_alice = alice - alice_change + bob_change
                new_bob = bob - bob_change + alice_change

                if new_alice == new_bob:
                    return [alice_change, bob_change]
                elif new_alice > new_bob:
                    br = bm - 1
                elif new_alice < new_bob:
                    bl = bm + 1