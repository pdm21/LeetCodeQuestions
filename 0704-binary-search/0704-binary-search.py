class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        
        while left <= right:
            median = (left + right) // 2
            
            # median == target
            if nums[median] == target:
                return median # median is the index answer
            # median is too big
            elif nums[median] > target:
                right = median - 1
            # median is too small, target is larger
            else:
                left = median + 1
        
        # target not found
        return -1