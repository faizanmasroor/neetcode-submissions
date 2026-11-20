class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        found = dict()
        i = 0
        for num in nums:
            if target - num in found:
                return [found[target - num], i]
            found[num] = i
            i += 1
        