class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        result = 0
        for i in range(1, n):
            if prices[i] > prices[i-1]:
                result += (prices[i]-prices[i-1])
        return result
#122-LEETCODE