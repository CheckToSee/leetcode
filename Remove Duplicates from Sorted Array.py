class Solution:
    def removeDuplicates(nums):
        numsLength = len(nums)
        trail = 0
        k = 0
        dupCheck = []

        for i in range(numsLength):
            if nums[i] not in dupCheck:
                dupCheck.append(nums[i])
                nums[k] = dupCheck[k]
                k += 1
            else:
                trail += 1

        return k
