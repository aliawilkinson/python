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
        # look at each character
        # see if the current value is in the non repeating substring variable concurrent_substring
        # if it is, prev. length of substrin is len
        # else, add to string and keep evaluating
        # if this substring is longer than last substring
        # replace with longer substring
        # else
        # if at the end of the string, return substring
        answer = 0
        string_length = len(s)
        if string_length == 1:
            answer = 1
        if string_length > 1:
            longest_substring = 0
            concurrent_substring = []
            # for s[i] in s:
            for i in range(string_length):
                if not s[i] in concurrent_substring:
                    concurrent_substring.append(s[i])
                elif len(concurrent_substring) > longest_substring:
                    longest_substring = len(concurrent_substring)
                    concurrent_substring = [s[i]]

            if len(concurrent_substring) > longest_substring or longest_substring == 0:
                answer = len(concurrent_substring)
            else:
                answer = longest_substring
        return answer

    def testTask(self):
        test_cases = {
            # 0: {
            #     "Input": "abcabcbb",
            #     "Output": 3
            # },
            # 1: {
            #     "Input": "bbbbb",
            #     "Output": 1
            # },
            # 2: {
            #     "Input": "pwwkew",
            #     "Output": 3
            # },
            # 3: {
            #     "Input": " ",
            #     "Output": 1
            # },
            # 4: {
            #     "Input": "",
            #     "Output": 0
            # },
            # 5: {
            #     "Input":"au",
            #     "Output": 2
            # },
            # 6: {
            #     "Input": "aab",
            #     "Output": 2
            # },
            7: {
                "Input": "dvdf",
                "Output": 3
            }
        }
        passed = 0
        failed = 0
        for i in test_cases:
            code_answer = self.lengthOfLongestSubstring(test_cases[i]["Input"])
            if test_cases[i]["Output"] == code_answer:
                passed += 1
                print("Success!, code answer was: ", code_answer,
                      " right answer was: ", test_cases[i]["Output"])
            else:
                failed += 1
                print("Failed, code answer was: ", code_answer,
                      " right answer was ", test_cases[i]["Output"])
        print("Passed ", passed, " tests, Failed ", failed,
              " tests, success rate: ", (passed/(passed+failed))*100, "%")


task = Solution()
answer = task.testTask()
