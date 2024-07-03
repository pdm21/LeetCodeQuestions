class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i, j = 0, 0
        # if we hit a 0 at j, i stays put, find non-zero, swap, i = j
        while j < len(nums):
            if nums[j] != 0:
                nums[i], nums[j] = nums[j], nums[i] 
                i += 1
            j += 1
            
        return nums