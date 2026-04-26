from collections import Counter

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        c = Counter(nums)
        for key,freq in c.items():
            if freq > 1:
                return True
        return False