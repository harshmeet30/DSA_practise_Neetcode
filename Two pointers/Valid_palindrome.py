
class Solution:
    def isPalindrome(self, s: str) -> bool:
        l,r = 0, len(s)-1
        while l < r:
            while l<r and not self.alphanum(s[l]):
                l+=1
            while r >l and not self.alphanum(s[r]):
                r-=1
            if s[l].lower() != s[r].lower():
                return False
            l+=1
            r-=1
        return True
    
    def alphanum(self, c):
        return ((ord('A') <= ord(c) <=ord('Z')) or 
                (ord('a') <= ord(c) <=ord('z')) or
                (ord('0') <= ord(c) <=ord('9'))  )


###Alternate

# class Solution:
#     def isPalindrome(self, s: str) -> bool:
#         s = ''.join(c.lower() for c in s if c.isalnum())

#         i = 0
#         j = len(s)-1
#         if len(s)==0:
#             return True
#         while i< j :
#             if s[i] != s[j]:
#                 return False
#             i+=1
#             j-=1
#         return True
