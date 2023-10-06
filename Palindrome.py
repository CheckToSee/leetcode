class Solution(object):
    def isPalindrome(s):
        extracted_phrase = ''.join(filter(str.isalnum, str(s.lower())))
        length = len(extracted_phrase)
        start = 0
        length-=1
        while start<length:
            if not extracted_phrase[start] == extracted_phrase[length]:
                return False
            else:
                length-=1
                start+=1
        return True