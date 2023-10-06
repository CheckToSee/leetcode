class Solution(object):
    def mergeAlternately(word1, word2):
        len1 = len(word1)
        len2 = len(word2)
        counter = 0
        ans = ""

        if len1==len2:
            while(counter<len2):
                ans += word1[counter] + word2[counter]
                counter+=1
        elif len1>len2:
            while(counter<len2):
                ans += word1[counter] + word2[counter]
                counter+=1
            ans += word1[counter:]
        else:
            while(counter<len1):
                ans += word1[counter] + word2[counter]
                counter+=1
            ans += word2[counter:]
        return ans