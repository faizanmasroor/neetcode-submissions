class Solution:
    def isPalindrome(self, s: str) -> bool:
        valid = set()
        for i in range(ord('A'), ord('Z') + 1):
            valid.add(chr(i))
        for i in range(ord('a'), ord('z') + 1):
            valid.add(chr(i))
        for i in range(ord('0'), ord('9') + 1):
            valid.add(chr(i))
        l = 0
        while l < len(s) and s[l] not in valid:
            l += 1
        r = len(s) - 1
        while r >= 0 and s[r] not in valid:
            r -= 1
        print(l, r)
        while l < r:
            if s[l].lower() != s[r].lower():
                return False
            l += 1
            while l < len(s) and s[l] not in valid:
                l += 1
            r -= 1
            while r >= 0 and s[r] not in valid:
                r -= 1
        return True
        