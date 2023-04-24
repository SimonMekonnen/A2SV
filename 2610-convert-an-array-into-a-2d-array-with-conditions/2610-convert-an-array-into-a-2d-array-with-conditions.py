class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        arr = Counter(nums)
        ans = []
        while sum(arr.values() ) > 0:
            now = []
            for i in arr:
                if arr[i] != 0:
                    now.append(i)
                    arr[i] -= 1
            ans.append(now)
        return ans