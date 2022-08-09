class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if (len(s) != len(t)):
             return False
        map = {}
        for i in range(0,len(s)):    
            if(not s[i] in map):
                if(not t[i] in map):
                    map[s[i]] = t[i]
                    print(map)
                else:
                    return False
            elif (map[s[i]] != t[i]):
                return False
        return True
"""
Given two strings s and t, determine if they are isomorphic.
Two strings s and t are isomorphic if the characters in s can be replaced to get t.
All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.

d e
d g

map = {
b:b
a:a
d:b
}



"""

