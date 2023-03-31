class Solution:
    def countPrimes(self, n: int) -> int:
        
        prime = [1 for i in range(n)]
        if n == 0 or n == 1:
            return 0
        i = 2
        while i <= int(n**0.5):
            j = i * i
            if prime[i]!=0:
                while j < n:
                    prime[j] = 0
                    j += i
            if i == 2:
                i += 1
            else:
                i += 2
        return sum(prime) - 2
            
            