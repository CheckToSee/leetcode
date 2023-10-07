# FIXME: make it work run properly in leetcode
class Solution:
    def removeDuplicates(nums):
        numLength = len(nums)
        trail = 0
        k = 0
        dupCheck = []
        for i in range(numLength):
            if nums[i] not in dupCheck:
                dupCheck.append(nums[i])
                k += 1
            else:
                trail += 1
        for i in range(trail):
            dupCheck.append('_')
        nums = dupCheck
        print(nums)
        return k

print(Solution.removeDuplicates([0,0,1,1,1,2,2,3,3,4]))
