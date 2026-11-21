class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        longest = 0
        l = 0
        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)
            maxf = max(count.values())
            while (r - l + 1) - maxf > k:
                count[s[l]] = count[s[l]] - 1
                l += 1
                maxf = max(count.values())
            longest = max(longest, r - l + 1)
        return longest
