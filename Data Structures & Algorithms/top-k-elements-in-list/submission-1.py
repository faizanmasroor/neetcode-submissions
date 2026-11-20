class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqs = dict()
        for num in nums:
            freqs[num] = freqs.get(num, 0) + 1

        bucket = list()
        for i in range(len(nums) + 1):
            bucket.append(list())

        for num, freq in freqs.items():
            bucket[freq].append(num)

        res = list()
        i = len(bucket) - 1
        while i >= 0 and len(res) < k:
            res += bucket[i]
            i -= 1

        return res
        