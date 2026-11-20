class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre = [0] * len(nums)
        post = [0] * len(nums)
        running_prod = 1
        for i in range(len(nums)):
            running_prod *= nums[i]
            pre[i] = running_prod
        running_prod = 1
        for i in range(len(nums) - 1, -1, -1):
            running_prod *= nums[i]
            post[i] = running_prod
        res = []
        for i in range(len(nums)):
            if i == 0:
                res.append(post[1])
            elif i == len(nums) - 1:
                res.append(pre[len(nums) - 2])
            else:
                res.append(pre[i - 1] * post[i + 1])
        return res
