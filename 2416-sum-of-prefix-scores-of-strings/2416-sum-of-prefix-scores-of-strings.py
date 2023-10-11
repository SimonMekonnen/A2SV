class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        tree = Trie()
        for i in words:
            tree.insert(i)
        arr = []
        for i in words:
            arr.append(tree.startsWith(i))
        return arr
    
class TrieNode:
    def __init__(self):
        self.is_end = False
        self.children = [None for _ in range(26)]
        self.count = 0

class Trie:
    def __init__(self):
        self.root = TrieNode()
    def insert(self, word: str) -> None:
        cur = self.root
        for i in range(len(word)):
            car = ord(word[i]) - ord('a')
            if not cur.children[car]:
                cur.children[car] = TrieNode()
            cur = cur.children[car]
            cur.count += 1
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
        ans = 0
        for ch in prefix:
            idx = ord(ch) - ord('a')
            cur = cur.children[idx]
            ans += cur.count
        return ans