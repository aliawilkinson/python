from typing import List


class Solution:
    def twoSum(self, nums, target):
        """
        Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
        You may assume that each input would have exactly one solution, and you may not use the same element twice.
        You can return the answer in any order.
        Test Cases:

            Example 1:
            Input: nums = [2,7,11,15], target = 9
            Output: [0,1]
            Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

            Example 2:
            Input: nums = [3,2,4], target = 6
            Output: [1,2]

            Example 3:
            Input: nums = [3,3], target = 6
            Output: [0,1]
        """
        values = {}
        for i, value in enumerate(nums):
            if target - value in values:
                return [values[target - value], i]
            else:
                values[value] = i

    def testTwoSum(self, nums=List[int], answer=[int]) -> bool:
        test_cases = {
            1: {
                "nums": [2, 7, 11, 15],
                "target": 9,
                "answer": [0, 1]
            },
            2: {
                "nums": [3, 2, 4],
                "target": 6,
                "answer": [1, 2]
            },
            3: {
                "nums": [3, 3],
                "target": 6,
                "answer": [0, 1]
            }
        }
        passed = 0
        failed = 0
        for case in test_cases:
            code_answer = self.twoSum(
                test_cases[case]["nums"], test_cases[case]["target"])
            if test_cases[case]["answer"] == code_answer:
                passed += 1
                print("Success!, code answer was: ", code_answer,
                      " right answer was: ", test_cases[case]["answer"])
            else:
                failed += 1
                print("Failed, code answer was: ", code_answer,
                      " right answer was ", test_cases[case]["answer"])
        print("Passed ", passed, " tests, Failed ", failed,
              " tests, success rate: ", (passed/(passed+failed))*100, "%")


missing_num = Solution()
answer = missing_num.testTwoSum()
