class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        
        while left <= right:
            median = (left + right) // 2
            if nums[median] == target:
                return median
            elif nums[median] < target:
                left = median + 1
            else:
                right = median - 1
        
        return -1