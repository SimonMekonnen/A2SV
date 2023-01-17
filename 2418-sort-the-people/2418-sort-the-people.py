class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:

        for i in range(len(names)):
            names[i] = (heights[i],names[i])
        
        names.sort(reverse = True)
        
        
                
        return [n for i,n in names]
