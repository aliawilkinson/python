from typing import List


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        Task: 
            Given a string s, find the length of the longest substring without repeating characters.

        Examples:
            Example 1:
            Input: s = "abcabcbb"
            Output: 3
            Explanation: The answer is "abc", with the length of 3.

            Example 2:
            Input: s = "bbbbb"
            Output: 1
            Explanation: The answer is "b", with the length of 1.

            Example 3:
            Input: s = "pwwkew"
            Output: 3
            Explanation: The answer is "wke", with the length of 3.
            Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

        PseudoCode:
            store nonrepeating substring in list concurrent_substring 
            store longest substring in longest_substring
        """
        # least the answer can be is 0
        answer = 0
        
        # index_map stores the current index of a character
        index_map = {}

        # num of letters in the unique substr
        count = 0
        
        # iterate
        for i in range(len(s)):
            # if the value is in the index map ex: a
            if s[i] in index_map:
                # take the count of char in the substr or the index of the letter
                # we broke on, whatever is bigger
                count = max(index_map[s[i]], count)

            # compare the last recorded answer and the index we are on minus the num
            # we have already found + 1 to account for str len
            answer = max(answer, i - count + 1)

            # set the char as the key and the count of substr it is
            index_map[s[i]] = i + 1

        return answer

    def testTask(self):
        test_cases = {
            0: {
                "Input": "abcabcbb",
                "Output": 3
            },
            1: {
                "Input": "bbbbb",
                "Output": 1
            },
            2: {
                "Input": "pwwkew",
                "Output": 3
            },
            3: {
                "Input": " ",
                "Output": 1
            },
            4: {
                "Input": "",
                "Output": 0
            },
            5: {
                "Input":"au",
                "Output": 2
            },
            6: {
                "Input": "aab",
                "Output": 2
            },
            7: {
                "Input": "dvdf",
                "Output": 3
            }
        }
        passed = 0
        failed = 0
        for count in test_cases:
            code_answer = self.lengthOfLongestSubstring(test_cases[count]["Input"])
            if test_cases[count]["Output"] == code_answer:
                passed += 1
                print("Success!, code answer was: ", code_answer,
                      " right answer was: ", test_cases[count]["Output"])
            else:
                failed += 1
                print("Failed, code answer was: ", code_answer,
                      " right answer was ", test_cases[count]["Output"])
        print("Passed ", passed, " tests, Failed ", failed,
              " tests, success rate: ", (passed/(passed+failed))*100, "%")


task = Solution()
answer = task.testTask()
