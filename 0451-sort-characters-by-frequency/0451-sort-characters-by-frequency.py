class Solution:
    def frequencySort(self, s: str) -> str:
        characters = Counter(s)
        chars =  [(v,k) for k,v in characters.items()]
        chars.sort(reverse=True)
        ans = ""
        for i,j in chars:
            ans+=j*i
        return ans
        