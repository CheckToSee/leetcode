class Solution(object):
    def kidsWithCandies(candies, extraCandies):
        ans = []
        greatest = 0

        for candy in candies:
            if candy>greatest:
                greatest = candy

        for candy in candies:
            if candy + extraCandies >= greatest:
                ans.append(True)
            else:
                ans.append(False)
        
        return ans    