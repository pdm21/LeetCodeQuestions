class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i, j, longest = 0, 0, 0
        d = {}
        while j < len(s):
            if s[j] in d and d[s[j]] >= i:
                # update i to last occurence of s[j] + 1
                i = d[s[j]] + 1
            
            # update d[s[j]] to new occurence
            d[s[j]] = j
            
            # calculate longest
            longest = max(longest, j - i + 1)
            j += 1
        
        return longest