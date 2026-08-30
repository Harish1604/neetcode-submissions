class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)
        maxi = 0
        for num in numset:
            if num-1 not in numset:
                length = 1
                current = num
            
                while current+1 in numset:
                    length+=1
                    current+=1
                maxi = max(maxi,length)
        return maxi


        