class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        ans = [0 for _ in range(len(pref))]
        ans[0] = pref[0]
        tally = ans[0]
        for i in range(1, len(pref)):
            ans[i] = pref[i] ^ tally
            tally ^= ans[i]
        return ans