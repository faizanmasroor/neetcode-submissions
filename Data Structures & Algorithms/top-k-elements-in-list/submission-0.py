class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = dict()
        for num in nums:
            freq[num] = freq.get(num, 0) + 1

        res = list()

        for i in range(k):
            max = -1
            next_num = 0
            for k, v in freq.items():
                if v > max:
                    max = v
                    next_num = k
            del freq[next_num]
            res.append(next_num)

        return res