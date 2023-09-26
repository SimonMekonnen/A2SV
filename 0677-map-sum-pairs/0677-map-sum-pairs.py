class MapSum:

    def __init__(self):
        self.tree = Trie()
        self.dic = defaultdict(int)
    def insert(self, key: str, val: int) -> None:
        
        self.tree.insert(key,val,self.dic[key])
        self.dic[key] = val
        
    def sum(self, prefix: str) -> int:
        return self.tree.startsWith(prefix)

        
        
class TrieNode:
    def __init__(self):
        self.is_end = False
        self.children = [None for _ in range(26)]
        self.count = [0 for i in range(26)]

class Trie:
    def __init__(self):
        self.root = TrieNode()
    def insert(self, word: str,val:int,t:int) -> None:
        cur = self.root
        for i in range(len(word)):
            car = ord(word[i]) - ord('a')
            if not cur.children[car]:
                cur.children[car] = TrieNode()
            cur = cur.children[car]
            cur.count[car] += val - t
     
            
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
        for ch in prefix:
            idx = ord(ch) - ord('a')
            if not cur.children[idx]:
                return 0
            cur = cur.children[idx]
            t = cur.count[idx]
        return t

# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)