class Solution:
    def longestPalindrome(self, s: str) -> str:

        def split(left, right):
            while left>=0 and right<len(s)and s[left] == s[right]:
                right +=1
                left-=1
            return s[left+1:right]
        
        res = ""

        for i in range(len(s)):
            p1 = split(i,i)
            p2 = split(i,i+1)

            if len(p1) > len(res):
                res = p1
            
            if len(p2) > len(res):
                res = p2
        return res
                
        