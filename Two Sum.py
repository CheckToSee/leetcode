class Solution(object):
    def twoSum(nums, target):
        length = len(nums)
        ans = []
        for i in range(length):
            for j in range(i+1,length):
                if nums[i]+nums[j] == target:
                    ans = [i,j]
        return ans