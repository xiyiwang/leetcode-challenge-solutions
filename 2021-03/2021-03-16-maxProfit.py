"""
LeetCode Challenge: Best Time to Buy and Sell Stock with Transaction Fee
(2021-03-16)

You are given an array prices where prices[i] is the price of a given 
stock on the ith day, and an integer fee representing a transaction 
fee.

Find the maximum profit you can achieve. You may complete as many 
transactions as you like, but you need to pay the transaction fee 
for each transaction.

Note: You may not engage in multiple transactions simultaneously 
(i.e., you must sell the stock before you buy again).

Constraints:
- 1 < prices.length <= 5 * 10^4
- 0 < prices[i], fee < 5 * 10^4
"""

# DP approach: runtime - 704 ms (faster than 66.85%)
def maxProfit(prices, fee):
    cash, hold = 0, -prices[0]
    # cash: cash in hand when not hold
    # hold: cash in hand when hold

    for i in range(len(prices)):
        cash = max(cash, hold + prices[i] - fee)
        """
        2 possibilities when not hold on day i:
          a) not hold on day i-1: 
             cash(i) = cash(i-1)
          b) hold on day i-1 and sell on day i:
             cash(i) = hold(i-1) + prices[i] - fee
        """
        hold = max(hold, cash - prices[i])
        """
        2 possibilities when hold on day i:
          a) hold on day i-1:
             hold(i) = hold(i-1)
          b) not hold on day i-1 and buy in on day i:
             hold(i) = cash(i-1) - prices[i]
        """

    return cash


# 8
# prices = [1,3,2,8,4,9]
# fee = 2

# 6
prices = [1,3,7,5,10,3]
fee = 3

print(maxProfit(prices, fee))