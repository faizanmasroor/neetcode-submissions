class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        self.selectionSort(nums)
        print(nums)
        result = []
        prevFirstVal = math.inf
        for i in range(len(nums) - 2):
            if nums[i] != prevFirstVal:
                targetSum = -nums[i]
                j = i + 1
                k = len(nums) - 1
                currSum = nums[j] + nums[k]
                while j < k:
                    if currSum == targetSum:
                        result.append([nums[i], nums[j], nums[k]])
                        j += 1
                        while j < len(nums) and nums[j] == nums[j - 1]:
                            j += 1
                        k -= 1
                        while k > i and nums[k] == nums[k + 1]:
                            k -= 1
                    elif currSum < targetSum:
                        j += 1
                    else:
                        k -= 1
                    if j >= len(nums) or k <= i:
                        break
                    currSum = nums[j] + nums[k]
            prevFirstVal = nums[i]
        return result;

        
    def selectionSort(self, nums: List[int]) -> None:
        for i in range(len(nums) - 1):
            indexOfMin = i
            for j in range(i, len(nums)):
                if nums[j] < nums[indexOfMin]:
                    indexOfMin = j
            temp = nums[i]
            nums[i] = nums[indexOfMin]
            nums[indexOfMin] = temp
