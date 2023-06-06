class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        ans = set()
       
        def bt(arr,taken):
            if len(arr) > len(tiles):
                return
            ans.add(tuple(arr))
            for i in range(len(tiles)):
                if i not in taken:
                    taken.add(i)
                    bt(arr + [tiles[i]],taken)
                    taken.remove(i)
        bt([],set())
 
        return len(ans) - 1
            
            
            
        