"""
LeetCode: Min Cost Climbing Stairs (2021-06-07)

You are given an integer array cost where cost[i] is the cost 
of ith step on a staircase. Once you pay the cost, you can either 
climb one or two steps.

You can either start from the step with index 0, or the step with 
index 1.

Return the minimum cost to reach the top of the floor.

Constraints:
- 2 <= cost.length <= 1000
- 0 <= cost[i] <= 999
"""
class Solution:
    # dp - O(N)
    def minCostClimbingStairs(self, cost: list) -> int:
        dp = [0] * (len(cost) + 1)
        for i in range(2, len(cost) + 1):
            dp[i] = min(dp[i-1] + cost[i-1], dp[i-2] + cost[i-2])
        return dp[-1]
    
    def minCostClimbingStairs2(self, cost: list) -> int:
        dp1 = dp2 = 0
        for i in range(len(cost)):
            dp1, dp2 = dp2, cost[i] + min(dp1, dp2)
        return min(dp1, dp2)

cost1 = [10,15,20] # 15
cost2 = [1,100,1,1,1,100,1,1,100,1] # 6
