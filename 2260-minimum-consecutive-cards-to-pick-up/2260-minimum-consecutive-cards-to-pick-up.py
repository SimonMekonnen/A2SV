class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        right = 0
        left = 0
        seen = set()
        ans = math.inf
        while right < len(cards):
            if cards[right] in seen:
                seen.remove(cards[left])
                ans = min(ans,len(seen))
                left+=1
            else:
                seen.add(cards[right])
                right+=1
        ans = ans + 2 if ans!=math.inf else -1
        return ans
            
        