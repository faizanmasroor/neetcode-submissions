class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_ = -math.inf
        for i in range(len(prices) - 1):
            for j in range(i + 1, len(prices)):
                if prices[j] - prices[i] > max_:
                    max_ = prices[j] - prices[i]
        return max(0, max_)
