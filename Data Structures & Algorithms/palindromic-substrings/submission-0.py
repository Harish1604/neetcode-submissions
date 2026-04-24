class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 0
        def equal(left,right):
            nonlocal count
            while left >=0 and right < len(s) and s[left] == s[right]:
                left -=1
                count+=1
                right +=1

            return s[left+1:right]

        for i in range(len(s)):
            equal(i,i)
            equal(i,i+1)

        return count
       