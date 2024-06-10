#LEETCODE-121
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not  prices:
            return 0
        maxprofit = 0
        minpurchase = prices[0]
        for i in range(len(prices)):
            maxprofit = max(maxprofit, prices[i]-minpurchase)
            minpurchase = min(minpurchase, prices[i])
        return maxprofit