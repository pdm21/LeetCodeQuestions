class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for x in range(len(nums)):
            curr_num = nums[x]
            diff = target - curr_num
            if diff in d.keys():
                return [d.get(diff)] + [x]
            else:
                d[curr_num] = x
        return 0