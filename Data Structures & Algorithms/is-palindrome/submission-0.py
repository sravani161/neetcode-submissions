class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_list = []
        for i in s:
            if i.isalnum():
                s_list.append(i.lower())
        
        return s_list == s_list[::-1]