class Solution:
    def findComplement(self, num: int) -> int:
         return (-1 * (1 - 2 ** int.bit_length(num))) ^ num
        