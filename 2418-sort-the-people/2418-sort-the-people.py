class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:

        for i in range(len(names)):
            _max = i
            for j in range(i , len(names)):

                if heights[j] > heights[_max]:
                    
                    _max = j
            
            names[i],names[_max] = names[_max],names[i]
            heights[i],heights[_max] = heights[_max],heights[i]

                   
                
        return names
