class Solution:
    def romanToInt(self, s: str) -> int:
        """
        For example, 2 is written as II in Roman numeral, just two ones added together. 12 is written as XII, which is simply X + II. The number         27 is written as XXVII, which is XX + V + II.

        Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the               number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number           nine, which is written as IX. There are six instances where subtraction is used:

        I can be placed before V (5) and X (10) to make 4 and 9.
        X can be placed before L (50) and C (100) to make 40 and 90.
        C can be placed before D (500) and M (1000) to make 400 and 900.
        Given a roman numeral, convert it to an integer.
        """
        lookup = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }

        # I can be placed before V(5) and X(10) to make 4 and 9.
        # X can be placed before L(50) and C(100) to make 40 and 90.
        # C can be placed before D(500) and M(1000) to make 400 and 900.
        # "III", 012, starts at 2,
        # Input: s = "MCMXCIV"
        # 4 90 900 1000
        # Output: 1994

        sum = 0
        i = len(s) - 1
        if (s[0] == "M"):
                sum += lookup[s[0]]
                i-= 1
        while i >= 0:
            right_num = lookup[s[i]]
            if (i != 0):
                left_num = lookup[s[i-1]]
            else:
                left_num = 0
            if (left_num < right_num):
                sum += right_num - left_num
            else:
                sum += left_num + right_num
            i -= 2
        print(sum)
        return sum


sol1 = Solution()
# sol1.romanToInt("MCMXCIV")
# sol1.romanToInt("IV")
sol1.romanToInt("MCDLXXVI")

# input "MCDLXXVI"
# 6 20 550 1100 = 1676 
# 1000 400 
