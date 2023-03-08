class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):
        self.persons = persons
        self.times = times
        so = defaultdict(int)
        t = persons[0]
        for i in range(len(self.times)):
            so[self.persons[i]] += 1
            if so[self.persons[i]] >= so[t]:
                t = persons[i]
            persons[i] = t
            
   
            
    def q(self, t: int) -> int:
        
        c = bisect_left(self.times,t)
        if c >= len(self.persons):
            return self.persons[-1]
        return self.persons[c] if self.times[c] == t else self.persons[c - 1]
        
        
        
        


# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)