class Solution:
    def removeDuplicates(nums):
        numsLength = len(nums)
        k = 0
        dupCheck = []

        for i in range(numsLength):
            if nums[i] not in dupCheck:
                dupCheck.append(nums[i])
                nums[k] = dupCheck[k]
                k += 1

        return k
