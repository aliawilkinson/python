from typing import List


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
        track = {}
        # current center, right, left 
        right = len(s)-1
        middle = int((len(s)-1)/2)
        longest = 0
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
        
        middle = int((len(s)-1)/2)
        for i in range(middle):
        # check values next to middle
            right,left = movePointers(right,left)
            if (s[left] == s[right]):
                right,left = movePointers(right,left)
            else:
                right,left = movePointers(right,left)

        def movePointers(right,left):
            right = middle -1
            left = middle +1
            return right,left

            # if they are same, continue
            # if they are not, move to next possible value

        

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
            if test_cases[i]["Output"] == code_answer:
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
