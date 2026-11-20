class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        freq = {}
        for num in nums:
            freq[num] = freq.get(num, 0) + 1
        candidates = []
        for num in nums:
            if num - 1 not in freq:
                candidates.append(num)
        max_len = 0
        for cand in candidates:
            curr_len = 1
            while cand + 1 in freq:
                curr_len += 1
                cand += 1
            max_len = max(max_len, curr_len)
        return max_len