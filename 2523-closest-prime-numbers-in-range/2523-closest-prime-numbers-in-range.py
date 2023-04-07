class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        
        
           is_prime: list[bool] = [True for _ in range(right + 1)]
          
           is_prime[0] = is_prime[1] = False

           i = 2
           while i <= right:
                if is_prime[i]:
                    j = i * i
                    while j <= right:
                        is_prime[j] = False
                        j += i
                if i == 2:
                    i += 1
                else:
                    i += 2
           now = [i for i in range(len(is_prime)) if is_prime[i] == True]
           last = [-1 ,-1]

           for i in range(len(now) - 1):
                if now[i] >= left and now[i + 1] <= right:
                    if last == [-1,-1] or last[-1] - last[0] > now[i + 1] - now[i]:
                        last = [now[i],now[i + 1]]
           return last
        