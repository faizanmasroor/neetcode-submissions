class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        char_freqs = list()
        res = list()
        for s in strs:
            # print(s)
            char_freq = dict()
            for char in s:
                char_freq[char] = char_freq.get(char, 0) + 1
            # for k in char_freq.keys():
            #     print(k, char_freq[k])
            i = 0
            while i < len(char_freqs):
                if char_freq == char_freqs[i]:
                    break
                i += 1
            # print(s, i)
            if (i == len(res)):
                res.append([s])
                char_freqs.append(char_freq)
            else:
                res[i].append(s)
        return res
        