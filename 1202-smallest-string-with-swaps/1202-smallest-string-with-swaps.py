class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        parent = [i for i in range(len(s))]
        def find(x):
            cur = x
            while cur != parent[cur]:
                cur = parent[cur]
            
            while x != parent[x]:
                v = parent[x]
                parent[x] = cur
                x = v
            return cur
        def union(x,y):
            xparent = find(x)
            yparent = find(y)
            
            parent[xparent] = yparent
        dic = defaultdict(list)
        for x,y in pairs:
            union(x,y)
        for i in range(len(parent)):
            dic[find(i)].append(i)
        
        for i in dic:
            dic[i].sort(key = lambda x : s[x],reverse = True)
            
        ans = []
        for i in range(len(s)):
            now = dic[find(i)]
            ans.append(s[now.pop()])
        
        return "".join(ans)
            
       