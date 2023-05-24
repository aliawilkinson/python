from typing import List, OrderedDict


class Solution:

    def longestPalindrome(self, s: str) -> str:
        """
        Given a string s, return the longest palindromic substring in s.

        Example:

        Input: s = "babad"
        Output: "bab"
        Explanation: "aba" is also a valid answer.

        "babad"

        b:0
        0:b
        d:4
        4:d
        a: {1:2},{3:2}
        1:a,
        3:a,
        b:{0:1},{2:1},
        0:b,
        2:b

        check a, b

        a and b can be edges because they have two+ indicies
        if track[2]

        """
        # look at the letter
        # if the letter next to it is the same, check on either side of those letters
        # two same letters are a palindrome
        # if the next letters to the left and the right are different, return 
        # else, continue
        # if the new palindrome is longer than the last one set it to longest
        # else, go until the end of the string 
        # return longest palindrome

        # more considerations: 
            # can start from the middle since those could be the longest 
            # if we have a palindrome that is the same length as the str, return 
            # if we have a palindrome that is already longer than any more could be, return 


    def checkPointers(self, s, right, left):
        if (s[right] == s[left]):
            right, left = self.movePointers(right, left)

    def movePointers(self, right, left):
        right = right - 1
        left = left + 1
        return right, left

    def initPointers(self, middle):
        right = middle - 1
        left = middle + 1
        return right, left

    def testTask(self) -> bool:
        test_cases = {
            0: {
                "Input": "babad",
                "Output": "bab"
            },
            1: {
                "Input": "cbbd",
                "Output": "bb"
            }
        }
        passed = 0
        failed = 0
        for i in test_cases:
            code_answer = self.longestPalindrome(test_cases[i]["Input"])
            if len(test_cases[i]["Output"]) == len(code_answer):
                passed += 1
                print("Success!, code answer was: ", code_answer,
                    " right answer was: ", test_cases[i]["Output"])
            else:
                failed += 1
                print("Failed, code answer was: ", code_answer,
                    " right answer was ", test_cases[i]["Output"])
        print("Passed ", passed, " tests, Failed ", failed,
              " tests, success rate: ", (passed / (passed + failed)) * 100,
            "%")


task = Solution()
answer = task.testTask()
