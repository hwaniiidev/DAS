from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        """
        my solution:
        This function works by keeping track of two things: the lowest price seen so far reader
        and the best profit found profix.
        """
        profit = 0
        reader = 0

        # Then, this loop through each price in the list.
        for i in range(1, len(prices)):
            # If the current price is lower than reader, it updates reader to this new low
            # This is the new buy point
            if prices[reader] > prices[i]:
                reader = i
            # Otherwise, we check if selling at this price gives me a profit greater than current profit.
            # If it does, we update profit
            elif prices[i] - prices[reader] > profit:
                profit = prices[i] - prices[reader]
        return profit



sol = Solution()

# Example 1:
print(sol.maxProfit(prices=[7,1,5,3,6,4]))

# Example 2:
print(sol.maxProfit(prices=[7,6,4,3,1]))