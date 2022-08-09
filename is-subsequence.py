class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        """
        Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

        A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters               without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).
        test case:
        Input: s = "abc", t = "ahbgdc"
        Output: true
        Example 2:

        Input: s = "axc", t = "ahbgdc"
        Output: false
        """
        last_index = 0
        for i in range(len(s)):
            present_index = t.find(s[i],last_index) 
            last_index = present_index + 1
            if (present_index == -1):
                return False
        return True
        
        
        """
        s 0 a
        t 0 a
        
        start at 1
        
        s 1 b
        t 2 b
        
        s 2 c
        t 5 c
        
        reached the end of len(s), return true
        """