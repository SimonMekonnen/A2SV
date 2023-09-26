class WordDictionary:

    def __init__(self):
        self.tree = Trie()

    def addWord(self, word: str) -> None:
        self.tree.insert(word)
    def search(self, word: str) -> bool:
        myword = list(word)
        mydots = []
        for i in range(len(myword)):
            if myword[i] ==".":
                mydots.append(i)
        if len(mydots) == 0:
            return self.tree.search(word)
        
        elif len(mydots) == 1:
            c = 0
            for i in range(26):
                myword[mydots[0]] = chr(ord('a') + i)
                c |= self.tree.search("".join(myword))
                if c:
                    break
              
            return c
        else:
            c = 0
            for i in range(26):
                myword[mydots[0]] = chr(ord('a') + i)
                for j in range(26):
                    myword[mydots[1]]  = chr(ord('a') + j)
                    c |= self.tree.search(''.join(myword))
                    if c == 1:
                        break
            return c
                    
                    
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
# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)