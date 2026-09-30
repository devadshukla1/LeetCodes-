class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        clean=""

        for ch in s:
            if ch.isalnum():
                clean += ch.lower()
        
        rev=[] 
        
        for i in range(len(clean)-1,-1,-1):
            rev.append(clean[i])
        
        res = "".join(rev)

        return clean == res



        