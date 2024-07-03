class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        d = {}
        for num in nums:
            if num in d:
                d[num] += 1
                if d[num] > (len(nums) // 2):
                    return num
            else:
                d[num] = 1
        return max(sorted(d.items(), key=lambda x: x[1]))[0]