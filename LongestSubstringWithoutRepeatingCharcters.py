
"""
Given a string, find the length of the longest substring without repeating characters. For example, the longest substring without repeating letters for "abcabcbb" is "abc", which the length is 3. For "bbbbb" the longest substring is "b", with the length of 1.i
"""



class Solution:
    # @return an integer
    def lengthOfLongestSubstring(self, s):
        
        l  = 0
        d = {}
        m = 0
        
        for r,c in enumerate(s):
            t = d.get(c,None)
            if t is not None and t >= l:
                l = t + 1
            
            d[c] = r
            m = max(m,r-l+1)

        return m



