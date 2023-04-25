class SmallestInfiniteSet:

    def __init__(self):
        self.now = set([i for i in range(1,10001)])

    def popSmallest(self) -> int:
        m = min(self.now)
        self.now.remove(m)
        return m

    def addBack(self, num: int) -> None:
        self.now.add(num)
        


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)