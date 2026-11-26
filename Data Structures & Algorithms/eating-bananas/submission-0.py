class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        maxPile = piles[0]
        for pile in piles:
            maxPile = max(maxPile, pile)
        kLow = 1
        kHigh = maxPile
        while kLow < kHigh:
            kMid = (kLow + kHigh) // 2
            numHoursAtMid = self.hoursToEatAll(piles, kMid)
            if numHoursAtMid <= h:
                kHigh = kMid
            else:
                kLow = kMid + 1
        return kLow
        
    def hoursToEatAll(self, piles: List[int], k: int) -> int:
        result = 0
        for pile in piles:
            result += math.ceil(pile / k)
        return int(result)
