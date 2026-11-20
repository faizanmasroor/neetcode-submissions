class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_ = -math.inf
        l = 0
        r = 1
        while r < len(prices):
            if prices[r] < prices[l]:
                l = r
            elif prices[r] - prices[l] > max_:
                max_ = prices[r] - prices[l]
            r += 1
        return max(0, max_)
