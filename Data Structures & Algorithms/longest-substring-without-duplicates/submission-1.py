class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) < 2:
            return len(s)
        window = set()
        j = 0
        while j < len(s) and s[j] not in window:
            window.add(s[j])
            j += 1
        ans = j
        i = 0
        while j < len(s):
            if j - i > ans:
                ans = j - i
            while s[j] in window:
                window.remove(s[i])
                i += 1
            window.add(s[j])
            j += 1
        return max(j - i, ans)
