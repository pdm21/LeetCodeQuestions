class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        # convert to a string
        s = str(x)
        i, j = 0, len(s) - 1
        while i <= j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True