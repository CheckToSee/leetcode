class Solution(object):
    def largestAltitude(gain):
        start = 0
        ans = 0
        for i in gain:
            start += i
            if start>ans:
                ans = start
        return ans