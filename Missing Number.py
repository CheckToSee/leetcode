class Solution(object):
    def missingNumber(self, nums):
        length = len(nums)
        counter = 0
        
        for i in range(length + 1):
            if not i in nums:
                ans = i
                
        return ans