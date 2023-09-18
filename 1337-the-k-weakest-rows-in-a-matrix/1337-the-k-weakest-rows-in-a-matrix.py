class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]: 
        count  = []
        for row in range(len(mat)):
            c = 0
            for i in mat[row]:
                if i:
                    c += 1
                    
            count.append((c,row))
        count.sort()
        
        return [y for x,y in count[:k]]
        