class TrieNode:
    def __init__(self):
        self.is_end = False
        self.children = [ None for _ in range(26) ]



class Trie:

    def __init__(self):
        self.root = TrieNode()
        self.dic = set()
    def insert(self, word: str) -> None:
        cur = self.root
        for i in range(len(word)):
            car = ord(word[i]) - ord('a')
            if not cur.children[car]:
                cur.children[car] = TrieNode()
            cur = cur.children[car]
        cur.is_end = True
        self.dic.add(word)
    def search(self, word: str) -> bool:
        if word in self.dic:
            return True
        return False
    def startsWith(self, prefix: str) -> bool:
        
        cur = self.root
        pos = 1
        for ch in prefix:
            idx = ord(ch) - ord('a')
            if not cur.children[idx]:
                pos = 0
                break
            cur = cur.children[idx]
        return pos
    

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)