class Solution(object):
    def removeElement(self, nums, val):
        length = len(nums)
        counter = 0
        
        if not val in nums:
            return length
        
        for i in range(length):
            if nums[i] == val:
                counter += 1
        
        for i in range(counter):
            nums.remove(val)
        
        return length - counter