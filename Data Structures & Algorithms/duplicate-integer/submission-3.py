class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        freq = {}
        for val in nums:
            freq[val] = freq.get(val, 0) + 1
            if freq.get(val) > 1:
                return True
        return False