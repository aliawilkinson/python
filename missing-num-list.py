from typing import List


class Solution:
    def findMissingNum(self, nums: List[int]) -> int:
        """
        You are given an array containing 'n' distinct numbers taken from the range 0 to 'n'.
        Since the array has only 'n' numbers out of the total 'n+1' numbers, find the missing number.
        Test Cases:
            Input: nums = [3,0,1]
            Output: 2

            Input: nums = [0,1]
            Output: 2

            Input: nums = [9,6,4,2,3,5,7,0,1]
            Output: 8

            Input: [1]
            Output: [0]
        """

        sorted_nums = sorted(nums)
        if (sorted_nums[0] != 0):
            return 0
        missing_num = int()
        for i in range(len(sorted_nums)-1):
            if not (sorted_nums[i+1] == sorted_nums[i]+1):
                if (sorted_nums[i] != sorted_nums[i+1]):
                    missing_num = sorted_nums[i]+1
                    break
        if not (missing_num):
            missing_num = sorted_nums[len(sorted_nums) - 1] + 1
        return missing_num

    def testMissingNum(self, nums=List[int], answer=[int]) -> bool:
        test_cases = {
            3: [4, 2, 0, 1],
            2: [0, 1],
            8: [9, 6, 4, 2, 3, 5, 7, 0, 1],
            0: [1]
        }
        passed = 0
        failed = 0
        for right_answer in test_cases:
            code_answer = self.findMissingNum(test_cases[right_answer])
            if right_answer == code_answer:
                passed+=1
                print("Success!, code answer was: ", code_answer,
                      " right answer was: ", right_answer)
            else:
                failed+=1
                print("Failed, code answer was: ", code_answer,
                      " right answer was ", right_answer)
        print("Passed ", passed , " tests, Failed ", failed, " tests, success rate: ", (passed/passed+failed)*100, "%" )


missing_num = Solution()
answer = missing_num.testMissingNum()
