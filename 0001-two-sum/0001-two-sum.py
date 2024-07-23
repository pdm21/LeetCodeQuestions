class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for x in range(len(nums)):
            diff = target - nums[x]
            if diff in d:
                return [d.get(diff)] + [x]
            else:
                d[nums[x]] = x
        return 0