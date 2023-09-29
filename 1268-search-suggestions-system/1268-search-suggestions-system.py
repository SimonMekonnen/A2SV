class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        tree  = Trie()
        products.sort()
        for i in products:
            tree.insert(i)
       
        ans = tree.startsWith(searchWord)
        while len(ans) < len(searchWord):
            ans.append([])
        return ans
        
                
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
class TrieNode:
    def __init__(self):
        self.is_end = False
        self.children = [None for _ in range(26)]
        self.count = [0 for i in range(26)]
        self.ans = []

class Trie:
    def __init__(self):
        self.root = TrieNode()
    def insert(self, word: str) -> None:
        cur = self.root
        for i in range(len(word)):
            car = ord(word[i]) - ord('a')
            if not cur.children[car]:
                cur.children[car] = TrieNode()
            if len(cur.children[car].ans) < 3:
                heappush(cur.children[car].ans,word)
   
                
            cur = cur.children[car]
       
        
        cur.is_end = True
    def search(self, word: str) -> bool:
        cur = self.root
        for ch in word:
            idx = ord(ch) - ord('a')
            if not cur.children[idx]:
                return False
            cur = cur.children[idx]
        return cur.is_end
    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        t = 0
        arr = []
        for ch in prefix:
            idx = ord(ch) - ord('a')
            if not cur.children[idx]:
                return arr
           
            cur = cur.children[idx]
            arr.append(cur.ans)
            t = cur.count[idx]
        return arr
