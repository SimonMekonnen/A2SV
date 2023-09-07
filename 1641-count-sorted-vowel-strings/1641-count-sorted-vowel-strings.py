class Solution:
    def countVowelStrings(self, n: int) -> int:
        arr = [1,1,1,1,1]
        for i in range(2,n + 1):
            for j in range(len(arr)):
                arr[j] = sum(arr[j : ])     
        return sum(arr)