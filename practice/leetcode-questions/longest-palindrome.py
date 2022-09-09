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
        # track = {}
        # # current center, right, left
        # right = len(s) - 1
        # middle = int((len(s) - 1) / 2)
        # longest = 0
        # for left in range(len(s)):
        #     # get left val
        #     if (not s[left] in track):
        #         track[s[left]] = list()
        #         track[s[left]].append({left:left+1})
        #     else:
        #         # then we already know that there is 1 in there

        #         track[s[left]].append({left:left+1})
        #     track[left] = s[left]

        #     if (not s[right] in track):
        #         track[s[right]] = list()
        #         track[s[right]].append({right:right-1})
        #     else:
        #         # then we already know there is 1
        #         track[s[right]].append({right:right-1})
        #     track[right] = s[right]
        #     # get right val
        #     # get next to vals
        #     # if both those vals are on the same num, cont

        #     # move left towards middle
        #     right = right-1

        # for middle in range

        middle = int((len(s) - 1) / 2)
        right = middle - 1
        left = middle + 1
        palindromes = list()
        longest = str()
        current_pal = str()
        for i in range(middle):
            # check values next to middle
            # "babad", 2:b is middle
            right, left = self.initPointers(middle)
            # 1:a and 3:a
            if (s[right] == s[left]):
                current_pal = s[right:left+1]
                right, left = self.movePointers(right, left)
                self.checkPointers(s,right,left)
            else:
                if (len(longest) == len(s)):
                    break
                if (len(longest) > len(current_pal)):
                    longest = current_pal
                # new middle
                middle = right
                self.initPointers(middle)
                right, left = self.movePointers(right, left)
            
            if (len(longest) < len(current_pal)):
                    longest = current_pal
        return longest

        # we start in the middle because that's where the palindrome will be the longest 
        # if we have a large number palindrome and the index number to either edge is shorter, we skip

# Input: s = "babad"
#         Output: "bab"
#         Explanation: "aba" is also a valid answer.
# look at 2:b
# look at 3:a,1:a
# same, so add right-left+1


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
