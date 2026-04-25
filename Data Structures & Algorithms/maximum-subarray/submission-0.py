class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_val = nums[0]
        curr = nums[0]
        for i in range(1,len(nums)):
            curr = max(nums[i],curr+nums[i])
            max_val = max(max_val,curr)
        return max_val
        