class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        
        smallest = min(strs, key=len)
        for i in range(len(smallest)):
            char = smallest[i]
            for s in strs:
                if char != s[i]:
                    return smallest[:i]
        return smallest
                
        