class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "_" + s
        print(res)
        return res


    def decode(self, s: str) -> List[str]:
        i = -1
        j = 0
        res = []
        while i < len(s) and j < len(s):
            # dist = int(s[j])
            dist = int(s[j:].split("_")[0])
            num_digits = 1 if dist == 0 else math.floor(math.log10(dist)) + 1
            i = j + num_digits + 1
            j += dist + num_digits + 1
            res.append(s[i:j])
        return res

