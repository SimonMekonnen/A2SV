class BrowserHistory:

    def __init__(self, homepage: str):
        self.dic = {0:homepage}
        self.home = 0
        self.length = 1
        
        

    def visit(self, url: str) -> None:
        self.dic[self.home + 1] = url
        self.home += 1
        self.length = self.home + 1
   


    def back(self, steps: int) -> str:
        self.home = max(0,self.home - steps)
        return self.dic[self.home]
        

    def forward(self, steps: int) -> str:
    
        self.home = min(self.length - 1,self.home + steps)

        return self.dic[self.home]
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)