class Solution:
    def rob(self, nums):
        if len(nums) == 1:
            return nums[0]
        
        def rob_linear(arr):
            prev = 0
            curr = 0
            
            for num in arr:
                temp = max(curr, prev + num)
                prev = curr
                curr = temp
            
            return curr
        
        return max(
            rob_linear(nums[:-1]),  # exclude last
            rob_linear(nums[1:])    # exclude first
        )