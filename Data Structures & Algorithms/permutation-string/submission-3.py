class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1Count = {}
        for letter in s1:
            s1Count[letter] = s1Count.get(letter, 0) + 1
        # print(s1Count)

        count = dict(s1Count)
        for i in range(len(s1)):
            count[s2[i]] = count.get(s2[i], 0) - 1
            if count[s2[i]] == 0:
                del count[s2[i]]
        print(count)

        if not count:
            return True

        for i in range(len(s1), len(s2)):
            if s2[i] != s2[i - len(s1)]:
                count[s2[i]] = count.get(s2[i], 0) - 1
                count[s2[i - len(s1)]] = count.get(s2[i - len(s1)], 0) + 1
                if count[s2[i]] == 0:
                    del count[s2[i]]
                if count[s2[i - len(s1)]] == 0:
                    del count[s2[i - len(s1)]]
                if not count:
                    return True

        return False
        