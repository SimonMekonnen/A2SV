class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        table = Counter(words)
        words = [(-table[key],key) for key in table]
        heapify(words)
        ans = []
        while len(ans) < k:
            ans.append(heappop(words)[1])
        return ans
        
        
        
        