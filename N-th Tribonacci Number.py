class Solution(object):
    def tribonacci(n):
        triseq = [0, 1, 1]
        counter = 2
        ans = 0

        if n == 0:
            return 0
        elif n == 1:
            return 1
        elif n == 2:
            return 1
        
        n-=2

        while(True):
            ans = triseq[counter-2] + triseq[counter-1] + triseq[counter]
            counter+=1
            triseq.append(ans)
            n-=1
            if n == 0:
                break

        return ans