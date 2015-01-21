"""Given an array of integers, find two numbers such that they add up to a specific target number.

iThe function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2. Please note that your returned answers (both index1 and index2) are not zero-based.

You may assume that each input would have exactly one solution.

Input: numbers={2, 7, 11, 15}, target=9
Output: index1=1, index2=2"""


class Solution:
    # @return a tuple, (index1, index2)
    def twoSum(self, num, target):
        
        w = enumerate(num)
        s = sorted(w,key = lambda x: x[1])
        
        i = 0
        j = len(s)-1
        
        while i != j:
            if s[i][1] + s[j][1] == target:
                break
            elif s[i][1] + s[j][1] < target:
                i += 1
            else:
                j -= 1
        
        a,b = s[i][0],s[j][0]
            
        return a < b and (a+1,b+1) or (b+1,a+1)
        
