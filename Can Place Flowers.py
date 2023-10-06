class Solution(object):
    def canPlaceFlowers(flowerbed, n):
        length = len(flowerbed)
        firstLast = 0
        final_count = 0
        for test in flowerbed:
            if length == 1:
                if test==0:
                    final_count+=1
                    continue
            if firstLast == 0:
                if test == 0 and flowerbed[1]==0:
                    flowerbed[0] = 1
                    final_count+=1
                    
            elif firstLast == length-1:
                if test == 0 and flowerbed[firstLast-1]==0:
                    final_count+=1
                      
            elif test == 0:
                if flowerbed[firstLast-1] == 0 and flowerbed[firstLast+1] == 0:
                    flowerbed[firstLast] = 1
                    final_count+=1
                    
            firstLast+=1
        
        if n <= final_count:
            return True
        else:
            return False