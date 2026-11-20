class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        x = sorted(nums)
        for i, val in enumerate(x):
            if i < len(x) - 1 and val == x[i + 1]:
                return True
        return False