class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        parent = [i for i in range(len(accounts))]
        
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
        
        for i in range(len(accounts)):
            cur = accounts[i]
            for j in range(i + 1,len(accounts)):
                possible = accounts[j]
                if cur[0] == possible[0]:
                    for e in range(1,len(cur)):
                        if cur[e] in possible:
                            union(i,j)
                            break
        dic = defaultdict(list)
        for i in range(len(parent)):
            dic[find(i)].append(i)
        ans = []
        for i in dic:
            merged = dic[i]
            toadd = []
            for i in merged:
                toadd.extend(accounts[i][1:])
            another = [accounts[merged[0]][0]]
            another.extend(sorted(set(toadd)))
            ans.append(another)
        
        return ans
        
                    
                
        