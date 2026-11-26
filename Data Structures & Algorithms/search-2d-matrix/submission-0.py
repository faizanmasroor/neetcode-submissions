class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        numRows = len(matrix)
        numCols = len(matrix[0])
        left = 0
        right = numRows - 1
        while right - left > 1:
            mid = (right + left) // 2
            diff = target - matrix[mid][0]
            if diff == 0:
                return True
            if diff < 0:
                right = mid - 1
            else:
                left = mid
        if left == right or matrix[right][0] > target:
            return self.binarySearch(matrix[left], target)
        return self.binarySearch(matrix[right], target)

    def binarySearch(self, nums: List[int], target: int) -> bool:
        left = 0
        right = len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            diff = target - nums[mid]
            if diff == 0:
                return True
            if diff < 0:
                right = mid - 1
            else:
                left = mid + 1
        return nums[left] == target
        