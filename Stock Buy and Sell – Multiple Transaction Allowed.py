The cost of stock on each day is given in an array price[]. Each day you may decide to either buy or sell the stock at price[i], you can even buy and sell the stock on the same day. Find the maximum profit that you can get.

Note: A stock can only be sold if it has been bought previously and multiple stocks cannot be held on any given day.

Examples:

Input: prices[] = [100, 180, 260, 310, 40, 535, 695]
Output: 865
Explanation: Buy the stock on day 0 and sell it on day 3 => 310 – 100 = 210. Buy the stock on day 4 and sell it on day 6 => 695 – 40 = 655. Maximum Profit = 210 + 655 = 865.

Input: prices[] = [4, 2, 2, 2, 4]
Output: 2
Explanation: Buy the stock on day 3 and sell it on day 4 => 4 – 2 = 2. Maximum Profit = 2.
=============================================================================

from typing import List

class Solution:
    def maximumProfit(self, prices: List[int]) -> int:
        # Initialize profit to 0
        profit = 0
        
        # Iterate through the price array
        for i in range(1, len(prices)):
            # If the current price is higher than the previous one, add the difference to profit
            if prices[i] > prices[i - 1]:
                profit += prices[i] - prices[i - 1]
        
        return profit
