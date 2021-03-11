""""
LeetCode Challenge: Coin Change (2021-03-11)

You are given coins of different denominations and a total 
amount of money amount. Write a function to compute the 
fewest number of coins that you need to make up that amount. 
If that amount of money cannot be made up by any combination 
of the coins, return -1.

You may assume that you have an infinite number of each kind 
of coin.

Constraints:
- 1 <= coins.length <= 12
- 1 <= coins[i] <= 2^31 - 1
- 0 <= amount <= 10^4
"""

# Dynamic Programming Solution - runtime: 1924 ms (faster than 18.04%)
def coinChange(coins, amount):
    def dp(amount, cache = {}):
        if amount == 0: return 0
        if amount < 0: return float("inf")
        else: 
            if amount not in cache:
                cache[amount] = min(dp(amount - coin) + 1 for coin in coins)
            return cache[amount]
    return dp(amount) if dp(amount) != float("inf") else -1

# Official Solution: Dynamic Programming - Bottom Up (1120 ms)
def coinChange2(coins, amount):
    dp = [float("inf")] * (amount + 1)
    dp[0] = 0

    for coin in coins:
        for x in range(coin, amount + 1):
            dp[x] = min(dp[x], dp[x - coin] + 1)

    return dp[amount] if dp[amount] != float("inf") else -1
