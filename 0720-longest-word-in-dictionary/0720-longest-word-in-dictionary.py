class Solution:
    def longestWord(self, words: List[str]) -> str:
        
        dic = set(words)
        words.sort()
        ans = ""
        for i in range(len(words)):
            pos = 1
            for j in range(len(words[i])):
                if words[i][0:j+1] not in dic:
                    pos = 0
            if pos and len(ans) < len(words[i]):
                ans = words[i]
        return ans        
        
        
        
        
        
        
        
        
        
        
class TrieNode:
    def __init__(self):
        self.is_end = False
        self.children = [ None for _ in range(26) ]



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
        for ch in prefix:
            idx = ord(ch) - ord('a')
            if not cur.children[idx]:
                return False
            cur = cur.children[idx]
            
        return True