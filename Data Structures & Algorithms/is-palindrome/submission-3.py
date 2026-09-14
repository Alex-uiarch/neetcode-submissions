class Solution:
    def isPalindrome(self, s: str) -> bool:

        lst = ''
        for x in s:
            if x != " " and x != '?' and x != '.' and x != ',' and x != '!' and x != "'" and x != ';' and x != ':':
                lst += x.lower()

        if  lst == lst[::-1]:
            return True
        return False

        
