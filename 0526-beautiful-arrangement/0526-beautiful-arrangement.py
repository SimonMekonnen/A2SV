class Solution:
    def countArrangement(self, n: int) -> int:
        count = 0
        def bt(mask):
            nonlocal count
            if int.bit_count(mask) == n:
                count += 1
                return 
            
            for i in range(1,n + 1):
                c = 1 << (i - 1)
                num = int.bit_count(mask)
                if c & mask == 0 and\
                (i % (num + 1) == 0 or \
                 (num + 1) % i == 0) :
                    mask |= c
                    bt(mask)
                    mask ^= c
        bt(0)
        return count
    