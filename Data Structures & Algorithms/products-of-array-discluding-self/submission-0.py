class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod = prod_excl0 = 1
        cnt_zeros = 0
        for num in nums:
            prod *= num
            if num != 0:
                prod_excl0 *= num
            else:
                cnt_zeros += 1
            if cnt_zeros == 2:
                return [0] * len(nums)
        res = []
        for num in nums:
            if num == 0:
                res.append(prod_excl0)
            else:
                res.append(int(prod / num))
        return res

        