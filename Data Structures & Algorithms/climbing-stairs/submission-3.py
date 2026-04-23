class Solution:
    def climbStairs(self, n: int) -> int:
        stairNum = [0]*n
        if n <= 1: return n

        stairNum[0] = 1
        stairNum[1] = 2
        
        for i in range(2,n):
            stairNum[i] = stairNum[i-1] + stairNum[i-2]

        return stairNum[-1]