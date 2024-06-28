class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        for x in range(len(digits) - 1, -1, -1):
            if x == 0:
                if digits[x] < 9:
                    digits[x] += 1
                    return digits
                else:
                    return [1] + [0] * len(digits)
            elif digits[x] < 9:
                digits[x] += 1
                return digits
            elif digits[x] == 9:
                digits[x] = 0
        return 0
            