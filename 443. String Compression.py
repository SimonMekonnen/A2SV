class Solution:
    def compress(self, chars: List[str]) -> int:
        c = len(chars)
        left,right = 0 , 0
        while right < c:
            count = 0
            curr =  chars[right]
            while right < c and curr==chars[right]:
                count+=1
                right+=1
            chars[left] = curr
            left+=1
            if count == 1:
                continue
            ch =  str(count)
            for i in ch:
                chars[left] = i
                left+=1
        return left